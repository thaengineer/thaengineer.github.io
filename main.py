#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')


@app.route('/about')
def about():
	return render_template('about.html', title='About')


if __name__ == '__main__':
	app.run(debug=True)
