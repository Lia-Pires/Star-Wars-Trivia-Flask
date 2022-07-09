from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from model import db, save_db



app = Flask(__name__)



@app.route("/")
def home():
    return render_template('home.html', questions=db)


@app.route('/questions/<int:index>')
def questions_view(index):

    try:
        questions_db = db[index]
        return render_template('quiz.html', question=questions_db, index=index, max_index=len(db) - 1)

    except IndexError:
        abort(404)


# Adding a question
@app.route('/add_new_question', methods=['GET', 'POST'])
def add_question():

    if request.method == 'POST':

        question_dict = {
            "question": request.form['question'],
            "answer": request.form['answer']
        }

        db.append(question_dict)
        save_db()

        return redirect(url_for('questions_view', index=len(db) - 1))

    else:
        return render_template('add_question.html')


# Removing a Question
@app.route('/remove_a_question/<int:index>', methods=['GET', 'POST'])
def remove_question(index):
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for('home'))

        else:
            return render_template("remove_question.html", question=db[index])

    except IndexError:
        abort(404)


# REST API for Multi-Page App
@app.route('/api/question/')
def api_question_list():
    return jsonify(db)


@app.route('/api/question/<int:index>')
def api_question_detail(index):
    try:
        return db[index]

    except IndexError:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
