#!python
import flask

app=flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return flask.render_template("home.html")

@app.route('/calculator', methods=['GET'])
def calculator():
    return flask.render_template('calculator.html')

@app.route("/calculator", methods=["POST"])
def calculate():
    exp=flask.request.form['exp']
    return flask.render_template('calculator.html', perexp=exp, pervalue=eval(exp))

app.run()
