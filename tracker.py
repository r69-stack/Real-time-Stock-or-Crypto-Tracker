import yfinance as yf
import time
def get_live_price(ticker):
    try:
        # Fetches data for the symbol (e.g., 'BTC-USD' or 'AAPL')
        data = yf.Ticker(ticker)
        price = data.fast_info['last_price']
        return round(price, 2)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

symbol = 'BTC-USD' 
print(f"--- Tracking {symbol} Live ---")
while True:
    current_price = get_live_price(symbol)
    if current_price:
        print(f"Current {symbol} Price: ${current_price}")
    time.sleep(10)
