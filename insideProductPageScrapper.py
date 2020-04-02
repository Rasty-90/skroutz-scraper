#
#Use this scraper when scraping info from a specific product page
#

from bs4 import BeautifulSoup
import requests
import json

def singleSearch(shopOwner,listing):

    url = listing["link"]
    response=requests.get(url,timeout=10)
    content=BeautifulSoup(response.content,"html.parser")
    products = []

    for product in content.findAll('li', attrs={"class":"cf card js-product-card"}):
        productObject = {
            "shop": product.find('div', attrs={"class": "shop-name"}).text.encode('utf-8').decode('utf-8'),
        }
        products.append(productObject)

    if products[0]["shop"]!=shopOwner:
        return ( " single : To προϊόν υπάρχει σε χαμηλότερη τιμή")
    else:
        return (" single : Έχουμε την καλύτερη τιμή")