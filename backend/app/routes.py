from flask import Blueprint, request, jsonify
from .data_processing import *
from .arima_model import train_arima_model, hyperparameter_tuning, make_prediction

main = Blueprint('main', __name__)

@main.route('/api/stock', methods=['POST'])
def get_stock_data_and_jsonify():
    # TODO: add a check here to look at what data we already have in 
    # sqlite, if we need to grab new data from yf do it, if not
    # just pull from db.
    data = request.json
    symbol = data.get('symbol')
    period = data.get('period', '6mo')
    steps = int(request.json.get('steps', 5))
    try:
        stock_data = fetch_stock_data(symbol, period)
        stock_data, mean, std = normalize_data(stock_data, ['Open', 'High', 'Low', 'Close', 'Volume'])
        stock_data = create_lag_features(stock_data, lags=5)
        stock_data = create_rolling_features(stock_data)
        stock_data.dropna(inplace=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    # Assume the best order is already known or retrained
    #best_pdq = hyperparameter_tuning(stock_data, 'Close')
    #print(best_pdq)
    best_pdq = (30, 3, 4)  # For simplicity; should ideally be fetched from previous training
    column_to_fit = 'Close' # Assumed to be close, maybe mutable later
    mean = mean.loc[column_to_fit]
    std = std.loc[column_to_fit]
    model_fit = train_arima_model(stock_data, 'Close', best_pdq)
    predictions = make_prediction(model_fit, steps)
    predictions.name="Close"

    df = pd.concat([stock_data, predictions])
    df.fillna(0, inplace=True)
    # Convert to JSON for front end display
    result = df.to_dict(orient='records')
    return jsonify(result)

@main.route('/api/train_arima', methods=['POST'])
def train_arima():
    symbol = request.json['symbol']
    df = get_preprocess_store_data(symbol)

    best_pdq = hyperparameter_tuning(df, 'Close')
    model_fit = train_arima_model(df, 'Close', best_pdq)

    return jsonify({'message': 'ARIMA model trained successfully', 'order': best_pdq})

@main.route('/api/predict_arima', methods=['POST'])
def predict_arima():
    symbol = request.json['symbol']
    period = request.json.get('period', '1mo')
    steps = int(request.json.get('steps', 5))
    #df = get_preprocess_store_data(symbol, period)
    stock_data = fetch_stock_data(symbol, period)
    stock_data, mean, std = normalize_data(stock_data, ['Open', 'High', 'Low', 'Close', 'Volume'])
    stock_data = create_lag_features(stock_data, lags=5)
    stock_data = create_rolling_features(stock_data)
    stock_data.dropna(inplace=True)

    # Assume the best order is already known or retrained
    best_pdq = (10, 2, 4)  # For simplicity; should ideally be fetched from previous training
    column_to_fit = 'Close' # Assumed to be close, maybe mutable later
    mean = mean.loc[column_to_fit]
    std = std.loc[column_to_fit]
    model_fit = train_arima_model(stock_data, 'Close', best_pdq)
    predictions = make_prediction(model_fit, steps)

    predictions = [denormalize_prediction(p, mean, std) for p in predictions.tolist()]

    return jsonify({'symbol': symbol, 'predictions': predictions})