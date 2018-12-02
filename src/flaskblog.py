from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World! <br> sonu"


@app.route("/about")
def about():
    return "how are you? <br> fine"


app.run(debug=True)
