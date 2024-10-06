import requests
from celery import shared_task
from .models import InputData
from datetime import datetime

ALPHA_VANTAGE_API_KEY = 'HHH0G60N4G7B62XV'  # Replace with your Alpha Vantage API key

@shared_task
def update_live_stock_prices():
    stocks = InputData.objects.all()
    for stock in stocks:
        try:
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock.stockCode}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}"
            response = requests.get(url)
            data = response.json()

            # Fetch the latest time series data
            time_series = data.get('Time Series (1min)', None)
            if time_series:
                latest_time = sorted(time_series.keys())[0]
                current_price = time_series[latest_time]['4. close']

                # Update the stock price and last updated time
                stock.live_price = current_price
                stock.last_updated = datetime.now()
                stock.save()

                print(f"Updated {stock.stockCode}: Price = {current_price}")
            else:
                print(f"No data returned for {stock.stockCode}")

        except Exception as e:
            print(f"Error updating {stock.stockCode}: {e}")
