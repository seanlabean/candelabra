import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller, acf, pacf

def check_stationarity(timeseries):
    """Use Augmented Dickey-Fuller test for stationarity.
    return approximate p-value of rejecting null hypothesis 
    (non-stationary) (MacKinnon; 1994, 2010)."""
    result = adfuller(timeseries)
    return result[1] <= 0.05

def difference_data(df, column):
    df[f'{column}_diff'] = df[column].diff().dropna()
    return df

def train_arima_model(df, column, order):
    df.index = pd.to_datetime(df.index)  # Convert index to DateTimeIndex if not already
    df = df.asfreq('D')  # Set frequency to daily ('D'), or another appropriate frequency
    model = ARIMA(df[column], order=order)
    model_fit = model.fit()
    return model_fit

def hyperparameter_tuning(df, column):
    p = d = q = range(0, 3)
    pdq = [(x,y,z) for x in p for y in d for z in q]
    best_aic = float("inf")
    best_pdq = None
    for param in pdq:
        try:
            model_fit = train_arima_model(df, column, param)
            if model_fit.aic < best_aic:
                best_aic = model_fit.aic
                best_pdq = param
        except:
            continue
    return best_pdq

def make_prediction(model_fit, steps):
    return model_fit.forecast(steps=steps)