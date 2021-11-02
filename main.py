from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route("/contact", methods=['POST'])
def login():
    name = request.form['name']
    subject = request.form['subject']
    replyto = request.form['replyto']
    the_message = request.form['message']

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

