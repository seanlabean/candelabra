import pandas as pd
import yfinance as yf
from .databases import StockData, db

def fetch_stock_data(symbol, period="1mo"):
    """
    Given a stock symbol, return 1 month (default) of stock data
    from Yahoo Finance API.
    """
    response = yf.Ticker(symbol)
    return response.history(period=period)

def normalize_data(df, columns):
    """
    Z-score nomralization (standardization) 
    Returns a pandas dataframe with mean 0 and standard 
    deviation of 1, as well as the original mean and std.
    """
    mean = df[columns].mean()
    std = df[columns].std()
    df[columns] = (df[columns] - mean) / std
    return df, mean, std

def denormalize(value, mean, std):
    """
    Inverse of normalize_data.
    """
    return (value * std) + mean

def create_lag_features(df, lags, column='Close'):
    """
    Generate lag features for a given dataframe.
    """
    for lag in range(1, lags + 1):
        df[f'lag_{lag}'] = df[column].shift(lag)
    return df

def create_rolling_features(df, window=5, column='Close'):
    """
    Generate rolling mean and standard deviation over 
    5 day (default) windows.
    """
    df[f'rolling_mean_{window}'] = df[column].rolling(window=window).mean()
    df[f'rolling_std_{window}'] = df[column].rolling(window=window).std()
    return df

def store_data_in_db(symbol, data):
    """
    Store stock data in SQLite instance. Rollback and 
    continue if failure occurs.
    """
    try:
        # Store in SQLite
        for index, row in data.iterrows():
            stock_record = StockData(
                symbol=symbol,
                date=index.strftime('%Y-%m-%d'),
                open=row['Open'],
                high=row['High'],
                low=row['Low'],
                close=row['Close'],
                volume=row['Volume'],
                lag_1=row.get('lag_1'),
                lag_2=row.get('lag_2'),
                lag_3=row.get('lag_3'),
                lag_4=row.get('lag_4'),
                lag_5=row.get('lag_5'),
                rolling_mean_5=row.get('rolling_mean_5'),
                rolling_std_5=row.get('rolling_std_5')
            )
            db.session.add(stock_record)
        
        db.session.commit()
    except Exception as e:
        db.session.rollback()

def get_preprocess_store_data(symbol, period):
    # TODO: add a check here to look at what data we already have in 
    # sqlite, if we need to grab new data from yf do it, if not
    # just pull from db.

    stock_data = fetch_stock_data(symbol, period)

    # Preprocessing
    stock_data, mean, std = normalize_data(stock_data, ['Open', 'High', 'Low', 'Close', 'Volume'])
    stock_data = create_lag_features(stock_data, lags=5)
    stock_data = create_rolling_features(stock_data)
    stock_data.dropna(inplace=True)
    store_data_in_db(symbol, stock_data)

    return stock_data