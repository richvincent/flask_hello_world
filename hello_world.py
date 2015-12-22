from flask import Flask
from os import environ

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"


@app.route("/hello/<name>")
def hi_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten. Awww...
        </p>
        <img src="https://placeholdit.imgix.net/~text?txtsize=33&txt=350%C3%97150&w=350&h=150">
    """
    return html.format(name.title())


@app.route("/jedi/<firstName>/<lastName>")
def jedi_name(firstName, lastName):
    #
    jediName = lastName[0:3] + firstName[0:2]
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten. Awww...
        </p>
        <img src="https://placeholdit.imgix.net/~text?txtsize=33&txt=350%C3%97150&w=350&h=150">
    """
    return html.format(jediName.title())


if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
