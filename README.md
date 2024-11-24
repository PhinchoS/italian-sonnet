# italian-sonnet
# M7-Poetry Slam


**Author**:Phincho Sherpa

**Last Updated**: November 24th, 2024

<img src="[https://media.tenor.com/j3tvsfkggVMAAAAM/soup-soup-time.gif](https://cdn.britannica.com/88/256588-050-069B5B0F/Dante-Alighieri-portrait-Divine-Comedy-Inferno.jpg)" width=100%>

**Title**: VitaSonnet
## Description
This system is designed to create and evaluate Petrarchan/Italian sonnet. Petrarchan sonnet known for its structure, follows ABBAABBACDCDCD format and consists of 14 lines. It uses multiple libraries for Natural Processing Language(NLP) and setiment analysis create a peom. The database of words and phrases are inspired by collection of poems in _Vita Nuova_ by Dante Alighieri, widely regarded as the father of the Italian language. It provides a strong foundation reflecting the themes of love, longing, and spiritual contemplation that characterizes much of Petrarchan poetry. Through the sentiment analysis, it analyzes the tone and mood for the languages. 

##Set up

Install:
pip install spacy
python -m spacy download en_core_web_sm

pip install pronouncing

pip install nltk
python -m nltk.downloader vader_lexicon wordnet omw-1.4

pip install vaderSentiment

##Challenges

I encountered in this project was the need to bring in a substantial amount of outside knowledge, particularly realted to the Italian language. Most of the well-established NLP libraries tend to have better support and datasets for English. I could not yet find the solution of finding right rhyme with Italian words because it depended on the phonetic sounds of the words, which is different between all languages. I could not find a way in which these could be coded. Furthermore while I could rely on Dante's Vita Nuova as a source of inspiration, the vocabulary and understanding is different from modern Italian. This experience helped me undertand the importace of understanding cultural and linguistic context when developing language models other than English.


##Scholary Papers

https://arxiv.org/pdf/2406.18906
Generating and Evaluating Emotionally Resonant Poetry with Fine-Grained Sentiment Control
This paper inspired me to use sentiment to evaluate the quality of generated sonnets because Petrach sonnets have positive emotions. It emphasizes  on how emotional undertones can affect the asthetic of a poem. 

https://www.cambridge.org/core/journals/natural-language-engineering/article/multilingual-extension-and-evaluation-of-a-poetry-generator/21725A79692D38105E6E455A39F99526
Multilingual Extension and Evaluation of a Poetry Generator
This paper inspired me on how to create a single line. Since I was only focused on generating 14-line sonnets. The paper's dicussion on adapting poetry generation to different linguistic rules and structures helped me explore on using different sentence structure to format the lines. It created a more flexible and varied sentence structure.

https://books.google.com/books?hl=en&lr=&id=w6UzDwAAQBAJ&oi=fnd&pg=PA332&dq=generate+non+English+poems&ots=e-xPYwAY7D&sig=rtAmiD0mHPr39LSDFcDlWoEFZ0Y#v=onepage&q&f=false
In this they used newspaper and work of bertsolaritza as an inspiring set, which motivated me to use Dante's well known Vita Nuova as an inspiring set.
