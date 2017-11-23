import pandas as pd
import numpy as np
import pandas_datareader.data as web
from fbprophet import Prophet
import datetime

#function to get stock data
def yahoo_stocks(symbol, start, end):
    return web.DataReader(symbol, 'yahoo', start, end)

def get_historical_stock_price(stock):
    print ("Getting historical stock prices for stock ", stock)
    
    #get 7 year stock data for Apple
    startDate = datetime.datetime(2010, 1, 4)
    endDate = datetime.datetime(2017, 11, 22)
    stockData = yahoo_stocks(stock, startDate, endDate)
    
    #url = "http://real-chart.finance.yahoo.com/table.csv?s=%s&ignore=.csv" %(stock)
    #print url
    return stockData


def main():
    stock = input("Enter stock name(ex:GOOGL, AAPL): ")
    df_whole = get_historical_stock_price(stock)
    
    df = df_whole.filter(['Close'])
    df['ds'] = df.index
    #log transform the ‘Close’ variable to convert non-stationary data to stationary.
    df['y'] = np.log(df['Close'])
    
    model = Prophet()
    model.fit(df)

    num_days = int(input("Enter no of days to predict stock price for: "))
    future = model.make_future_dataframe(periods=num_days)
    forecast = model.predict(future)

    #Prophet plots the observed values of our time series (the black dots), the forecasted values (blue line) and
    #the uncertainty intervalsof our forecasts (the blue shaded regions).
    
    plt = model.plot(forecast)
    plt.show()

    plt = model.plot_components(forecast)
    plt.show()
    
    #Plot the forecast in the original scale instead of log-transformed scale
    forecast_orig = forecast # make sure we save the original forecast data
    forecast_orig['yhat'] = np.exp(forecast_orig['yhat'])
    forecast_orig['yhat_lower'] = np.exp(forecast_orig['yhat_lower'])
    forecast_orig['yhat_upper'] = np.exp(forecast_orig['yhat_upper'])
    
    df['y_log'] = df['y'] #copy the log-transformed data to another column
    df['y'] = df['Close'] #copy the original data to 'y'
    
    model.plot(forecast_orig)
    
    df.set_index('ds', inplace=True)
    forecast.set_index('ds', inplace=True)
    
if __name__ == "__main__":
    main()