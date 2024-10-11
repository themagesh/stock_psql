import templates.yfainace.yfinance as yf

sbin = yf.Ticker("HDFCBANK.NS")

stock_info = sbin.history(period="1d")
current_price = stock_info['Close'].iloc[-1]

# Print the current stock price
print(current_price)
