from bs4 import BeautifulSoup
import requests
import json
#Use this scraper when scraping info from a specific product page


#Default search url is https://www.skroutz.gr/search?keyphrase=
url="https://www.skroutz.gr/s/17697577/Durex-Surprise-Me-Variety-Box-40τμχ.html"
response=requests.get(url,timeout=5)
content=BeautifulSoup(response.content,"html.parser")
products = []

for product in content.findAll('li', attrs={"class":"cf card js-product-card"}):
    productObject = {
        "shop": product.find('div', attrs={"class": "shop-name"}).text.encode('utf-8').decode('utf-8'),
    }
    print(productObject)