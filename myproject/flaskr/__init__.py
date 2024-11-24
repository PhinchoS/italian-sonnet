from flask import (
    Flask, render_template
)
from .poem_maker import *
# from more_itertools import first_true
app = Flask(__name__)

@app.route("/")


def hello():
    return render_template(
        'website.html',
        my_poem=create_sonnet()
        )