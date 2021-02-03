from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    render_template("index.html", title="Super Bowl Prop Bet Pool")


@app.route("/bet", methods=['GET', 'POST'])
def bet():
    if request.method == 'GET':
        return all_bets()
    if request.method == 'POST':
        pass


@app.route("/props", methods=['GET', 'POST'])
def props():
    if request.method == 'GET':
        return all_props()
    if request.method == 'POST':
        pass


def all_bets():
    pass


def all_props():
    pass
