import pandas as pd 
import numpy as np 
import yfinance as yf 



def load_forex_data (symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data


ex = load_forex_data('EURCAD=X', '2023-01-01', '2023-10-01')



print (ex[1:5])


