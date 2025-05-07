#forex trading 

import time
import yfinance as yf
import datetime as dt 

short_window =5
long_window = 20 #window to calculate long term simple moving average 

initial_capital = 10000
position = 0
capital = initial_capital

forex_pair = 'EURUSD=X' 

try: 
    while True:
        data = yf.download(forex_pair, period='1d', interval='1m') #data for latest exchange rate every minute 
        data['SMA_SHORT'] = data['Close'].rolling(window=short_window).mean() # average of the Close prices over the last 5 minutes 
        data ['SMA_LONG'] = data['Close'].rolling(window=long_window).mean()
        time.sleep(60) #wait for 1 minute before next data fetch
        latest_data = data.iloc[-1] # iloc retrive the last row 

        if latest_data['SMA_SHORT'] > latest_data['SMA_LONG'] and position == 0:
            # Buy signal
            units_to_buy = capital / latest_data['Close']
            capital -= units_to_buy * latest_data['Close']
            position += units_to_buy
            print(f"Buying at {latest_data['Close']} on {latest_data.name}")
            
        elif latest_data['SMA_SHORT'] < latest_data['SMA_LONG'] and position > 0:
            # Sell signal
            capital = position * latest_data['Close']
            position = 0
            print(f"Selling at {latest_data['Close']} on {latest_data.name}")
except KeyboardInterrupt:
    pass
