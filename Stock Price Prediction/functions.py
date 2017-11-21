import pandas as pd
import pandas_datareader.data as web
import io
import numpy as np
import requests
import time
import datetime
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (15,5)
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

#Get stock data
def yahoo_stocks(symbol, start, end):
    return web.DataReader(symbol, 'yahoo', start, end)

#Add rows for missing dates
def add_missing_dates(dataframe, start, end):
    idx = pd.date_range(start, end)
    dataframe.index = pd.DatetimeIndex(dataframe.index)
    dataframe = dataframe.reindex(idx, fill_value='np.nan')
    return dataframe

#Convert the columns to numeric
def convert_to_numeric(dataframe):
    for col in dataframe:
        dataframe[col] = pd.to_numeric(dataframe[col], errors='coerce')
    return dataframe
                          
def interpolate(dataframe):
    features = list(dataframe)
    for feature in features:
        dataframe[feature] = dataframe[feature].interpolate()
    return dataframe  

#difference between the previous day and today's closing value
def prev_diff(dataframe):
    close = dataframe['Close']
    prev_diff = [0]
    for i in range(1, len(dataframe)):
        prev_diff.append(round((close[i]-close[i-1]),6))
    return prev_diff

def predict_prices(company):
    #get 7 year stock data for the input company
    startDate = datetime.datetime(2010, 1, 4)
    endDate = datetime.date.today()
    stockData = yahoo_stocks(company, startDate, endDate)
    stockMarketData = yahoo_stocks('^GSPC', startDate, endDate)
    stockData = add_missing_dates(stockData, startDate, endDate)
    stockMarketData = add_missing_dates(stockMarketData, startDate, endDate)
    stockDataNumeric = convert_to_numeric(stockData)
    stockMarketDataNumeric = convert_to_numeric(stockMarketData)
    stockDataInterpolated = interpolate(stockDataNumeric)
    stockMarketDataInterpolated = interpolate(stockMarketDataNumeric)
    stockDataInterpolated['prev_diff'] = prev_diff(stockDataInterpolated)            
    stockMarketDataInterpolated['sm_prev_diff'] = prev_diff(stockMarketDataInterpolated)             
    stockMarketDataInterpolated.columns = ['sm_open', 'sm_high', 'sm_low', 'sm_close', 'sm_adj_close', 'sm_volume', 'sm_prev_diff']             
    finalData = pd.concat([stockDataInterpolated, stockMarketDataInterpolated], axis=1)
    df_arima = finalData['Close']    
             
    model = ARIMA(df_arima, order=(5,1,1))
    model_fit = model.fit(disp=0)
    print(model_fit.summary())
    
    residuals = pd.DataFrame(model_fit.resid)
    residuals.plot()
    plt.show()
    residuals.plot(kind='kde')
    plt.show()
    print(residuals.describe())
                 
    X = df_arima.values
    Y = df_arima.index
    size = int(len(X) * 0.85)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order=(5,1,0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        y_Output = output[0]
        predictions.append(y_Output)
        obs = test[t]
        history.append(obs)
        #print('predicted=%f, expected=%f' % (y_Output, obs))
        
    error = mean_squared_error(test, predictions)
    print('Test MSE: %.3f' % error)
    
    # plot
    plt.plot(test, color='blue')
    plt.plot(predictions, color='red')
    plt.xlabel('Date')
    plt.ylabel('Closing Value in $')
    plt.show()
    
    # multi-step out-of-sample forecast
    forecast = model_fit.forecast(steps=7)[0]
    week_predictions = []
    day = 1
    for values in forecast:
        print('Day %d: %f' % (day, values))
        week_predictions.append(values)
        day += 1
    
    # plot
    fig, ax = plt.subplots()
    ax.plot(weekPredictions, color='red')
    plt.show()
    
    pltLength = int(len(Y)) - 1
    pltSize = int(len(Y)) - 30
    pltValues = Y[size: length]
    
    datemin = Y.date.min().year
    datemax = Y.date.max().year
    
    price_predictions = [{"label" : "Index", "value": [[datemin, datemax]]}, \
                         {"label" : "Actual Value", "value": [X]}, \
                         {"label" : "Predicted Value", "value": [predictions]}]
    
    return price_predictions