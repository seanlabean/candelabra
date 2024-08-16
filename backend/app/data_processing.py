import pandas as pd
import yfinance as yf

def fetch_stock_data(symbol, period="1mo"):
    response = yf.Ticker(symbol)
    return response.history(period=period)

def normalize_data(df, columns):
    df[columns] = (df[columns] - df[columns].mean()) / df[columns].std()
    return df

def create_lag_features(df, lags, column='Close'):
    for lag in range(1, lags + 1):
        df[f'lag_{lag}'] = df[column].shift(lag)
    return df

def create_rolling_features(df, window=5, column='Close'):
    df[f'rolling_mean_{window}'] = df[column].rolling(window=window).mean()
    df[f'rolling_std_{window}'] = df[column].rolling(window=window).std()
    return df