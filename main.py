#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask import url_for
import stripe

stripe.api_key     = "sk_test_51I1nUmGubTt6z2vkyMzHmlkyP8NvQMpBraXeHCYKnAjpBUyzoPtQzydyGQHUERQi83Yvfm8SkyenLewzG4G7Se770040C7kC57"
stripe.api_version = "2020-08-27"
stripe.max_network_retries = 2
app                = Flask(__name__)


# stripe
# 'pk_test_51I1nUmGubTt6z2vks0AdZylEM98F2VBD4slqsFwfP6OP4aqtnyy2ETPfsqrBoZYwf9F8JGQJq7DlTjNiNUZroGv200zJG9k2tp'
# 'sk_test_51I1nUmGubTt6z2vkyMzHmlkyP8NvQMpBraXeHCYKnAjpBUyzoPtQzydyGQHUERQi83Yvfm8SkyenLewzG4G7Se770040C7kC57'

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')


@app.route('/checkout')
def checkout():
	return render_template('checkout.html', title='Checkout')


@app.route('/charge')
def charge():
	return render_template('charge.html', title='Checkout')


@app.route('/about')
def about():
	return render_template('about.html', title='About')


if __name__ == '__main__':
	app.run(debug=True)
