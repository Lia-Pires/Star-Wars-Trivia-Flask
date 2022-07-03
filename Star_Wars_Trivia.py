from flask import Flask


app = Flask(__name__)


@app.route('/')
def welcome():
    return "This is my very first flask app"


@app.route('/cool')
def cool():
    return "Flask is cool"


counter = 0


@app.route('/view_count')
def view_count():
    global counter
    counter += 1
    return f"This page has been viewed {counter} times"


if __name__ == '__main__':
    app.run(debug=True)
