from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from price_tracker_api import pricetrackerApi

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(pricetrackerApi.addNewPriceData, 'interval', minutes=1)
    scheduler.start()