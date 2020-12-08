from price_tracker_app.models import Item
import requests
from bs4 import BeautifulSoup
import datetime
import json

def addItem(url):
    (name, price, today) = getItemData(url)
    prices = {
        "values": [
            {"date": today,"price": price}
        ]
    }
    item = Item(name=name, url=url, prices=prices)
    item.save()

def getItemData(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    price_float = float(price.replace('\xa0€','').replace('.','').replace(',','.'))
    
    today = (datetime.datetime.today()).strftime("%m/%d/%Y %H:%M:%S")
    return name, price_float, today