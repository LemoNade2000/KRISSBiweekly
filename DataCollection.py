import yahoofinance as yf
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, timezone
import seaborn as sns
import os   

def collectData(ticker): 
    start_date = "2022-01-01"
    end_date = "2022-11-01"
    data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
    data = data.drop(columns= ['High', 'Low', 'Open', 'Volume', 'Adj Close'], axis = 1)
    sns.lineplot(x = data.index, y = data['Close'])
    plt.savefig('{}.png'.format(ticker))
    data.to_csv("./Data/{}.csv".format(ticker))
    print(data)
    
os.makedirs('Data', exist_ok=True) 
collectData("TSLA")
collectData("^TNX")