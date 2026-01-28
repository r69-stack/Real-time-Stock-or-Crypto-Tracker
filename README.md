# Real-time-Stock-or-Crypto-Tracker
A project that tracks live crypto and stock prices using Python and SQL. It uses a Java backend to show the data and has a built-in ML model to guess where the price is headed next.Real-time market tracker: I used Python to grab live data, SQL to save it, and Java to build the API. It also uses Machine Learning to predict short-term price trends.
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
        
        # TODO: This is where you'll call your SQL insert function
        # save_to_db(symbol, current_price) 
        
    time.sleep(10)
