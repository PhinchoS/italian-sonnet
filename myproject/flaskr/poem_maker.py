import spacy
import os
import random
import pronouncing
from nltk.corpus import wordnet as wn
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime

nlp = spacy.load("it_core_news_sm")

peom_txt = open("database.txt","r")
poem = peom_txt.read()
poem = " ".join(poem.splitlines())


doc =nlp(poem)
nouns = [token.text for token in doc if token.pos_ == "NOUN"]
adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
verbs = [token.text for token in doc if token.pos_ == "VERB"]
adverbs = [token.text for token in doc if token.pos_ == "ADV"]
prepositions = [token.text for token in doc if token.pos_ == "ADP"]
articles = [token.text for token in doc if token.pos_ == "DET"]



# Different template structure I noticed in sonnet poems
templates = [
    "{article} {subject} {verb} {adverb} {preposition} {article} {object}",
    "{subject} {preposition} {article} {object}",
    "{subject} {verb} {adverb} {preposition} {adjective} {object}",
    "{article} {subject} {preposition} {object}"
]

sonnet = {"first_sequence": [], "second_sequence": []}

def sonnet_line():
    """
    randomly chooses a template structure and word for each line
    """
    template = random.choice(templates)
    line = template.format(
        subject = random.choice(nouns),
        verb = random.choices(verbs),
        object = random.choice(nouns),
        adverb = random.choice(adverbs),
        adjective = random.choice(adjectives),
        preposition = random.choice(prepositions),
        article = random.choice(articles)
    )
    return line.replace("['",'').replace("']",'')
def last_word(line):
    """
    returns last word of a sentence
    """
    doc = nlp(line)
    if len(doc) != 0:
        return str(doc[-1])
    else:
        return "Please re-run the code."

def rhymes(target_word):
    """returns list of rhyming words"""
    return pronouncing.rhymes(target_word)

def first_sequence(length):
    """create peom line with the rhyming scheme of ABBA ABBA"""
    for i in range (2):
        for i in range(length):
            line = sonnet_line()
            sonnet["first_sequence"].append(line)
        rhyme_list = []
        while not rhyme_list:
            line = sonnet_line()
            sonnet["first_sequence"][0] = line
            word = last_word(line)
            rhyme_list = rhymes(word)
        highest_similarity_word = highest_similarity(word, rhyme_list)
        sonnet["first_sequence"][3] = new_last_word(sonnet["first_sequence"][3], highest_similarity_word)
        rhyme_list.clear() #clearing rhyme list for a new line
        while not rhyme_list:
            line = sonnet_line()
            sonnet["first_sequence"][1] = line
            word = last_word(line)
            rhyme_list = rhymes(word)
        highest_similarity_word = highest_similarity(word, rhyme_list)
        sonnet["first_sequence"][2] = new_last_word(sonnet["first_sequence"][2],highest_similarity_word)
    return sonnet["first_sequence"]

def second_sequence(length):
    """create peom line with the rhyming scheme of CBC BCB"""
    for i in range(length):
        line = sonnet_line()
        sonnet["second_sequence"].append(line)
    rhyme_list = []
    while not rhyme_list:
        line = sonnet_line()
        sonnet["second_sequence"][0] = line
        word = last_word(line)
        rhyme_list = rhymes(word)
    highest_similarity_word = highest_similarity(word, rhyme_list)
    sonnet["second_sequence"][2] = new_last_word(sonnet["second_sequence"][2], highest_similarity_word)
    if highest_similarity_word in rhyme_list:
        rhyme_list.remove(highest_similarity_word) # make sure that second line doesn't have the same word
    highest_similarity_word = highest_similarity(word, rhyme_list)
    sonnet["second_sequence"][4] = new_last_word(sonnet["second_sequence"][4], highest_similarity_word)
    rhyme_list.clear()
    while not rhyme_list:
        line = sonnet_line()
        sonnet["second_sequence"][1] = line
        word = last_word(line)
        rhyme_list = rhymes(word)
    highest_similarity_word = highest_similarity(word, rhyme_list)
    sonnet["second_sequence"][3] = new_last_word(sonnet["second_sequence"][3], highest_similarity_word)
    if highest_similarity_word in rhyme_list:
        rhyme_list.remove(highest_similarity_word) # make sure that second line doesn't have the same word
    highest_similarity_word = highest_similarity(word, rhyme_list)
    sonnet["second_sequence"][5] = new_last_word(sonnet["second_sequence"][5], highest_similarity_word)
    return sonnet["second_sequence"]
    
def new_last_word(line, new_word):
    """replaes the the line with a new last word"""
    replace_word = last_word(line)
    return line.replace(replace_word, new_word)


def highest_similarity(word, rhyme_list):
    """calculates the rhyming word with highest similarity"""
    highest_similarity = 0.0
    highest_similarity_word = ""
   
    for i in rhyme_list: 
        synsets_word1 = wn.synsets(word, lang = 'ita')
        synsets_word2 = wn.synsets(i, lang = 'ita')
        for synset1 in synsets_word1:
            for synset2 in synsets_word2:
                if i == word:
                    rhyme_list.remove(i)
                similarity = wn.path_similarity(synset1,synset2)
                if similarity and similarity > highest_similarity:
                    highest_similarity = similarity
                    highest_similarity_word = i
    return highest_similarity_word

  

def evaluate():
    """
    evalutes the peom according to its sentiment and saves poem with the compound score
    of higher or equal to 0.5
    """
    poem_list = create_sonnet()
    poem_str = "\n".join(poem_list)
    analyzer = SentimentIntensityAnalyzer()
    analyzed = analyzer.polarity_scores(poem_str)
    compound_score = analyzed['compound']
    time_date = datetime.now().strftime("%m%Y, %H%M%S")
    if compound_score >= 0.5:
        folder_path = "past_poems/"
        file_path = os.path.join(folder_path,f"petrarchan_sonnet_{time_date}.txt")
        with open(file_path,"w") as file:
            file.write(poem_str)
        print("Poem saved")

def create_sonnet():
    """
    combining the firs sequence and secodn sequence to create a Italian sonnet poem
    """
    final_poem = first_sequence(4) + second_sequence(6)
    del final_poem[14:]
    final_poem.insert(4,"")
    final_poem.insert(9,"")
    final_poem.insert(13,"")
    poem = []
    for stanza in final_poem:
        poem.append(stanza)
    return poem
evaluate()  





    
        