from multipleSearchScrapper import multipleSearch
from insideProductPageScrapper import singleSearch
import pandas as pd


#static values
shopOwner="Aquario" #your own shop/your client's shop

#reading the file and converting it to Dict
products = pd.read_csv('listprod.csv')
productList =products.to_dict('records')

for listing in productList:
    if listing["searchType"]=="single":
        print (singleSearch(shopOwner,listing))
    else:
        print(multipleSearch(shopOwner,listing))
