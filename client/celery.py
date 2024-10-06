# stock_psql/celery.py
from celery import Celery
from celery.schedules import crontab

app = Celery('stock_psql')

# Periodic task to run every minute (or adjust as necessary)
app.conf.beat_schedule = {
    'fetch-stock-prices-every-1-second': {
        'task': 'stock_psql.tasks.fetch_and_update_stock_prices',
        'schedule': 1.0,  # 1-second interval
    },
}

