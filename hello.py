# import json


# with open('twitterData.json') as json_data:
#     jsonData = json.load(json_data)


# for i in jsonData:
#     print (i['date'])

from flask import Flask,url_for
app = Flask(__name__)


url_for('static', filename='style.css')
url_for('static', filename='scripts.js')
url_for('static', filename='index.html')


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

