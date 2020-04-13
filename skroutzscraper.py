from multipleSearchScrapper import multipleSearch
from insideProductPageScrapper import singleSearch

import csv

#static values
shopOwner="Aquario" #your own shop/your client's shop


with open('listprod.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    productList = reader

    for listing in productList:
        if listing["searchType"]=="single":
            print (singleSearch(shopOwner,listing))
        else:
            print(multipleSearch(shopOwner,listing))