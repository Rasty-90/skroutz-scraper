#
#Use this scraper when scraping multiple products from a search
#
from bs4 import BeautifulSoup
import requests

def multipleSearch(shopOwner,listing):

    #gets url from product listing
    url = listing["link"]
    response=requests.get(url,timeout=10)
    content=BeautifulSoup(response.content,"html.parser")
    products = []
    for product in content.findAll('div', attrs={"class": "card-content"}):
        productObject = {
            #use UTF-8 encoding to grab the greek characters, and UTF-8 decoding afterwards to get rid of the additional "b" character 
            #that spawns in front of every value after the encoding
            #partition at the end removes the article "στο" from the shop value
            "shop": product.find('span', attrs={"class": "shop-count"}).text.encode('utf-8').decode('utf-8').partition(' ')[2],
        }
        products.append(productObject)

    if products[0]["shop"]!=shopOwner:
        return (" To προϊόν υπάρχει σε χαμηλότερη τιμή") #returns that shop is NOT the first on the listings
    else:
        return (" Έχουμε την καλύτερη τιμή") #returns that shop is the first on the listings