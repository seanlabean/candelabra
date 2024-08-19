import pandas as pd
import yfinance as yf
from .databases import StockData, db

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

def get_preprocess_store_data(symbol, period):
    # TODO: add a check here to look at what data we already have in 
    # sqlite, if we need to grab new data from yf do it, if not
    # just pull from db.

    stock_data = fetch_stock_data(symbol, period)

    # Preprocessing
    stock_data = normalize_data(stock_data, ['Open', 'High', 'Low', 'Close', 'Volume'])
    stock_data = create_lag_features(stock_data, lags=5)
    stock_data = create_rolling_features(stock_data)
    stock_data.dropna(inplace=True)

    try:
        # Store in SQLite
        for index, row in stock_data.iterrows():
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
    return stock_data