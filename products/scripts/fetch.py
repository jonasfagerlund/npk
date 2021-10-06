import requests
from bs4 import BeautifulSoup

from products.models import Product

r = requests.get('https://www.snusbolaget.se/sok/siberia-80-degrees-white-dry-portion')

soup = BeautifulSoup(r.text, 'lxml')

def run():
    Product.objects.create(
        title=get_title(),
        price=get_price(),
        size=get_size(),
        nicotine_content=get_nicotine(),
        product_url='https://www.snusbolaget.se/sok/siberia-80-degrees-white-dry-portion',
        image_url=get_product_image()
    ).save()

def get_title():
    return soup.find('h1').text

def get_price():
    price_pane = soup.find('ul', class_='list-unstyled')
    list_item = price_pane.find('li')
    price = list_item.find(class_ = 'pull-right').text.strip()[:-3]
    formatted_price = price.replace(',', '.')
    return float(formatted_price)

def get_product_image():
    image_div = soup.find('div', class_ = 'product-image')
    image = image_div.find('img')
    return image['src']

content_table = bord = soup.find_all('td')

def get_size():
    size = content_table[11].text.strip()[:-2]
    formatted_size = size.replace(',', '.')
    return float(formatted_size)

def get_nicotine():
    amount = bord[7].text.strip()[:-5]
    formatted_amount = amount.replace(',', '.')
    return float(formatted_amount)

