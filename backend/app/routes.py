from flask import Blueprint, request, jsonify
from .data_processing import fetch_stock_data, normalize_data, create_lag_features, create_rolling_features

main = Blueprint('main', __name__)

@main.route('/api/stock', methods=['POST'])
def get_stock_data():
    data = request.json
    symbol = data.get('symbol')
    period = data.get('period', '1mo')
    stock_data = fetch_stock_data(symbol, period)

    # Preprocessing
    stock_data = normalize_data(stock_data, ['Open', 'High', 'Low', 'Close', 'Volume'])
    stock_data = create_lag_features(stock_data, lags=5)
    stock_data = create_rolling_features(stock_data)
    stock_data.dropna(inplace=True)

    # Convert to JSON
    result = stock_data.to_dict(orient='records')
    return jsonify(result)