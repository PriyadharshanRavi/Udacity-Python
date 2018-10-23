import requests
from bs4 import BeautifulSoup

def run(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094" + str(page)
        sourcecode = requests.get(url)
        plain_text = sourcecode.text
        soup = BeautifulSoup(plain_text,'html.parser')
        for link in soup.findAll('a', {'class': 'b-guidancecard__link'}):
            href = link.get('href')
            print(href)
        page += 1
run(1)