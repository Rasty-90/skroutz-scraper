from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Anna'}
    return render_template('index.html', title='Home', user=user)

@app.route('/newProduct')
def newProduct():
    user = {'username': 'Anna'}
    return render_template('newProduct.html', title='Home', user=user)