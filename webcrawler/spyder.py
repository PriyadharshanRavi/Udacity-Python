import requests
from bs4 import BeautifulSoup

def get_single_item_data(item_url):
    sourcecode = requests.get(item_url)
    plain_text = sourcecode.text
    soup = BeautifulSoup(plain_text,'html.parser')
    result = soup.findAll('span', {'id': 'prcIsum_bidPrice'})
    if len(result)<=0:
    	result = soup.findAll('span', {'id', 'prcIsum'})
    print(result)
    for item in result:
    	price = item.string
    	print(price)
    for link in soup.findAll('a'):
    	all_links = link.get('href') 
    	print(all_links)
    	

def run(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.ebay.com/b/HP-Laptops-Netbooks/175672/bn_2780154" + str(page)
        sourcecode = requests.get(url)
        plain_text = sourcecode.text
        soup = BeautifulSoup(plain_text,'html.parser')
        result = soup.findAll('a', {'class': 's-item__link'})
        for link in result:
            href = link.get('href')
            title = link.string
            print(href)
            print(title)
            get_single_item_data(href)
        page += 1  



run(3)

