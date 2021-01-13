# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 02:58:16 2020

@author: raden
"""
import pandas_datareader as dr 
import pandas as df
from matplotlib import pyplot as plt
from datetime import datetime
import numpy as np

"Mr. Gil's stock analysis"
while 1==1:
    print("please enter a ticker to recieve stock data")
    choice = input('')
    answer =dr.get_data_tiingo(choice, api_key = "##################")
    answer.reset_index(inplace=True)
    print(answer.head(-1))
    yaxis=answer.adjClose
    xaxis= answer.date
    plt.xlabel('data since 2015')
    plt.ylabel(str(choice)+ ' performance')
    plt.plot(xaxis, yaxis, linestyle = '-')
    plt.figure(figsize=(10, 8))
    plt.show()
    plt.close('all')
    start2= datetime(2019,4,1)
    end2 = datetime.today()
    answer =dr.get_data_tiingo(choice, start2, end2, api_key = "############################")
    answer.reset_index(inplace=True)    
    yaxis=answer.open
    xaxis= answer.date
    plt.xlabel('data since beginning of last year')
    plt.ylabel(str(choice)+ ' performance')
    plt.plot(xaxis, yaxis)
    plt.figure(figsize=(10, 10))
    plt.show()
    plt.close('all')
    start1= datetime(2020,1,1)
    end1 = datetime.today()
    answer =dr.get_data_tiingo(choice, start1, end1, api_key = "###############")
    answer.reset_index(inplace=True)
    print('This is the most recent stock data')
    yaxis=answer.open
    xaxis= answer.date
    plt.xlabel('data since beginning of year')
    plt.ylabel(str(choice)+ ' performance')
    plt.plot(xaxis, yaxis)
    plt.figure(figsize=(10, 8))
    plt.show()
    plt.close('all')
    def simple_rate_of_return(adjclose):
        daily_simple_ror = np.diff(adjclose)/adjclose[:-1]
        return daily_simple_ror*100
    #adjust = simple_rate_of_return(answer.adjClose.shift(-1))
    print('This is the simple rate of return:')
    answer['simpleror'] = simple_rate_of_return(answer['adjClose'])
    print( answer[['date','simpleror']])
    #daily_ror= answer['adjClose'].pct_change()*100
    #print(daily_ror.head(-1))
    
