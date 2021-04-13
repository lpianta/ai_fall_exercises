from flask import Flask, render_template, url_for, redirect, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/advice')
def advice():
    return render_template('advice.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/bookshelf')
def bookshelf():
    return render_template('bookshelf.html')


if __name__ == "__main__":
    app.run(debug=True)
