import plotly
plotly.tools.set_credentials_file(username='indirabobburi', api_key='5d5RcOxltJvD0QiLux1g')
plotly.__version__

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

#df = pd.read_csv('historical-data.csv')

#sample_data_table = FF.create_table(df.head())
#py.iplot(sample_data_table, filename='sample-data-table')

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

df_external_source = FF.create_table(df.head())
py.iplot(df_external_source, filename='df-external-source-table')
trace = go.Scatter(x = df['AAPL_x'], y = df['AAPL_y'],
                  name='Share Prices (in USD)')
layout = go.Layout(title='Apple Share Prices over time (2014)',
                   plot_bgcolor='rgb(230, 230,230)', 
                   showlegend=True)
fig = go.Figure(data=[trace], layout=layout)

py.iplot(fig, filename='apple-stock-prices')
