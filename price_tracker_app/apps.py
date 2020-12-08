from django.apps import AppConfig


class PriceTrackerAppConfig(AppConfig):
    name = 'price_tracker_app'
    
    def ready(self):
        from price_tracker_api import updater
        updater.start()
        
