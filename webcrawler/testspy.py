import requests
from bs4 import BeautifulSoup

def run(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.ebay.com/b/HP-Laptops-Netbooks/175672/bn_2780154" + str(page)
        sourcecode = requests.get(url)
        plain_text = sourcecode.text
        soup = BeautifulSoup(plain_text,'html.parser')
        for itemprice in soup.findAll('span', {'class': 's-item__price'}):
    		href = link.get('href')
            title = link.string
            print(href)
            print(itemprice.string)
        page+=1    

run(1)    		