#!python
import flask
import markdown

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

@app.route("/markdownrenderer/home", methods=["GET", "POST"])
def markdownhome():
    return flask.render_template("/markdownrenderer/home.html")

@app.route("/markdownrenderer/value", methods=["POST"])
def markdownrender():
    uploadmethod=flask.request.form["uploadmethod"]
    if uploadmethod=="text":
        rendertext=flask.request.form["markdown"]
    else:
        rendertext=flask.request.files["file-upload"].read().decode('utf-8')
    renderresult=markdown.markdown(rendertext)
    return flask.render_template("/markdownrenderer/value.html", renderfile=rendertext, renderresult=renderresult)

app.run(debug=True)
