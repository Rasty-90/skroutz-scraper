from flask import render_template,request
from multipleSearchScrapper import multipleSearch
from app import app
import csv
import pandas as pd


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
    df = pd.read_csv ('listprod.csv', encoding='utf8')
    productList=df.to_dict('records')
    results=[]
    for res in productList:
        showedRes = {
            "name": res["product"],
            "result": multipleSearch("Aquario",res)
        }
        results.append(showedRes)
    return render_template('compare.html', title='Σύγκριση τιμών', productList=results)

@app.route('/newProduct', methods=['POST'])
def my_form_post():
    prName = request.form['prName']
    skLink = request.form['skLink']
    searchType=request.form['searchType']
    fields=[prName,skLink,searchType]
    with open('listprod.csv','a', newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    return 'ok'


