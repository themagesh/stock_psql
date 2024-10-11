import yfinance as yf

stock='SBIN'

ticker = f"{stock}.NS"  
stock_ticker = yf.Ticker(ticker)
print(stock_ticker.info.get('earningsGrowth', 'N/A'))
print(stock_ticker.info.get('recommendationKey','N/A'))

# import yfinance as yf
# from django.shortcuts import render
# from datetime import datetime

# def stock_history_view(stock_code):
#     # Fetch the stock data for the last 1 year
#     ticker = yf.Ticker(stock_code)  # e.g., 'AAPL'
#     end_date = datetime.now().strftime('%Y-%m-%d')  # today's date
#     start_date = (datetime.now().replace(year=datetime.now().year - 1)).strftime('%Y-%m-%d')  # one year ago
    
#     # Fetch historical data for the last year
#     stock_history = ticker.history(period='1y')
#     print(stock_history)
#     # Create a list of dictionaries to send the data to the template
# stock_history_view('SBIN.ns')

  
