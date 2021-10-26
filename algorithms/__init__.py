import math
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.ar_model import AutoReg, AR
from statsmodels.tsa.arima.model import ARIMA
from pandas.plotting import autocorrelation_plot,lag_plot
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
import datetime as dt
from datetime import date
from datetime import timedelta
import yfinance as yf

from algorithms.get_data import crypto_data
from algorithms.mf_LSTM import lstm
from algorithms.mf_ARIMA import arima