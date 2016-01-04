from flask import Flask, render_template
import datetime
from os import environ

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"


@app.route("/hello/<name>")
def hi_person(name):
    return render_template('template.html', my_string="Hello Mode",
                           my_data=name,
                           current_time=datetime.datetime.now())


@app.route("/jedi/<firstName>/<lastName>")
def jedi_name(firstName, lastName):
    jediName = lastName[0:3] + firstName[0:2]
    return render_template('template.html', my_string="Jedi Identity",
                           my_data=jediName,
                           current_time=datetime.datetime.now())


if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
