from bs4 import BeautifulSoup
import requests
import json
#Use this scraper when scraping multiple products from a search

shopOwner="Aquario" #your own shop/your client's shop
#Default search url is https://www.skroutz.gr/search?keyphrase=
defaultUrl="https://www.skroutz.gr/search?keyphrase="
key = "Sera Vipan 100ml"
url = defaultUrl + key
response=requests.get(url,timeout=5)
content=BeautifulSoup(response.content,"html.parser")
products = []

for product in content.findAll('div', attrs={"class": "card-content"}):
   
    productObject = {
        #use UTF-8 encoding to grab the greek characters, and UTF-8 decoding afterwards to get rid of the additional "b" character 
        #that spawns in front of every value after the encoding
        "product": product.find('a', attrs={"class": "js-sku-link"}).text.encode('utf-8').decode('utf-8'),
        "price": product.find('a', attrs={"class": "js-sku-link sku-link"}).text.encode('utf-8').decode('utf-8'),
        "shop": product.find('span', attrs={"class": "shop-count"}).text.encode('utf-8').decode('utf-8').partition(' ')[2],
    }
    products.append(productObject)

#optional:save the results to a JSON file in order to handle the data later
if products[0]["shop"]!=shopOwner:
    print ( "To προϊόν υπάρχει σε χαμηλότερη τιμή")
else:
    print ("Έχουμε την καλύτερη τιμή")