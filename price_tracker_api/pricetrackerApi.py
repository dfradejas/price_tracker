from price_tracker_app.models import Item
from price_tracker_app.functions import getItemData
import datetime

def addNewPriceData():
    items = Item.objects.all()
    for item in items:
        (name,price,today) = getItemData(item.url)
        item.prices["values"].append({"date":today, "price":price })
        item.save()