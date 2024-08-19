import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller, acf, pacf

def check_stationarity(timeseries):
    """Use Augmented Dickey-Fuller test for stationarity.
    return approximate p-value of rejecting null hypothesis 
    (non-stationary) (MacKinnon; 1994, 2010)."""
    result = adfuller(timeseries)
    return result[1] <= 0.05