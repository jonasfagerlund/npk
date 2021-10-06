import math
from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from products.models import Product, Brand

options = Options()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

base_url = 'https://www.snusbolaget.se'

PRODUCTS_PER_PAGE = 28

def get_amount_of_pages():
    r = requests.get(base_url + '/snus')
    pagination_soup = BeautifulSoup(r.text, 'lxml')
    amount_of_products = pagination_soup.find('span', class_ = 'pages').text.strip()[20:-10]
    amount_of_pages = int(amount_of_products) / PRODUCTS_PER_PAGE
    amount_of_pages = int(math.ceil(amount_of_pages))
    return amount_of_pages


def get_page_source():
    driver.get(base_url + '/snus')
    sleep(2)
    driver.find_element_by_id('onetrust-accept-btn-handler').click();
    sleep(2)
    driver.find_element_by_link_text("No thanks, I'll stay here.").click();
    sleep(2)

    for x in range(get_amount_of_pages() -1):
        driver.find_element_by_link_text('Visa fler produkter').click();
        sleep(4)
    
    return driver.page_source

base_soup = BeautifulSoup(get_page_source(), 'lxml')

list_of_products = base_soup.find_all('a', class_ = 'image-box')

def run():
    for product in list_of_products:
        product_url = base_url + product['href']
        print(product_url)
        try:
            create_product(product_url)
        except (ValueError, AttributeError, IndexError):
            continue

def create_product(href):
    product_r = requests.get(href)
    product_soup = BeautifulSoup(product_r.text, "lxml")

    content_table = product_soup.find_all('td')

    Product.objects.create(
        title=get_title(product_soup),
        price=get_price(product_soup),
        size=get_size(content_table),
        nicotine_content=get_nicotine(content_table),
        product_url=href,
        image_url=get_product_image(product_soup),
        brand=get_brand(content_table)
    ).save()

def get_title(product_soup):
    return product_soup.find('h1').text

def get_price(product_soup):
    price_pane = product_soup.find('ul', class_='list-unstyled')
    list_item = price_pane.find('li')
    price = list_item.find(class_ = 'pull-right').text.strip()[:-3]
    formatted_price = price.replace(',', '.')
    return float(formatted_price)

def get_product_image(product_soup):
    image_div = product_soup.find('div', class_ = 'product-image')
    image = image_div.find('img')
    return image['src']

def get_size(table):
    size = table[11].text.strip()[:-2]
    formatted_size = size.replace(',', '.')
    return float(formatted_size)

def get_nicotine(table):
    amount = table[7].text.strip()[:-5]
    formatted_amount = amount.replace(',', '.')
    return float(formatted_amount)

def get_brand(table):
    brand_name = table[1].text.strip()
    obj, brand = Brand.objects.get_or_create(title=brand_name)
    obj.save()
    return obj
