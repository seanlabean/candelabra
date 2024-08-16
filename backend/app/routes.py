from flask import Blueprint, request, jsonify
from .data_processing import fetch_stock_data, normalize_data, create_lag_features, create_rolling_features
from .models import StockData, db

main = Blueprint('main', __name__)

@main.route('/api/stock', methods=['POST'])
def get_stock_data():
    # TODO: add a check here to look at what data we already have in 
    # sqlite, if we need to grab new data from yf do it, if not
    # just pull from db.
    data = request.json
    symbol = data.get('symbol')
    period = data.get('period', '1mo')
    stock_data = fetch_stock_data(symbol, period)

    # Preprocessing
    stock_data = normalize_data(stock_data, ['Open', 'High', 'Low', 'Close', 'Volume'])
    stock_data = create_lag_features(stock_data, lags=5)
    stock_data = create_rolling_features(stock_data)
    stock_data.dropna(inplace=True)
    stock_data['Date'] = stock_data.index.strftime('%Y-%m-%d')

    for index, row in stock_data.iterrows():
        stock_record = StockData(
            symbol=symbol,
            date=index,
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

    # Convert to JSON for front end display
    result = stock_data.to_dict(orient='records')
    return jsonify(result)