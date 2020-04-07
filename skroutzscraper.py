from multipleSearchScrapper import multipleSearch
from insideProductPageScrapper import singleSearch
import json 

#static values
shopOwner="Aquario" #your own shop/your client's shop

with open('productList.json','r', encoding='utf8') as json_file: #reads list of products
    data = json.load(json_file) 
    productList = data


for listing in productList:
    if listing["searchType"]=="single":
        print (singleSearch(shopOwner,listing))
    else:
        print(multipleSearch(shopOwner,listing))