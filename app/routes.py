from flask import render_template,request
from app import app
import json

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Anna'}
    return render_template('index.html', title='Home', user=user)

@app.route('/newProduct')
def newProduct():
    return render_template('newProduct.html', title='Διαχείριση προϊόντων')

@app.route('/compare')
def compare():
    with open('productList.json','r', encoding='utf8') as json_file: #reads list of products
        data = json.load(json_file) 
        productList = data
    return render_template('compare.html', title='Σύγκριση τιμών', productList=productList)

@app.route('/newProduct', methods=['POST'])
def my_form_post():
    prName = request.form['prName']
    skLink = request.form['skLink']
    searchType=request.form['searchType']
    return (prName+','+skLink+","+searchType)