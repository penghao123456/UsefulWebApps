#!python
import flask

app=flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return flask.render_template("home.html")


