from flask import Blueprint, request, jsonify
from .data_processing import get_preprocess_store_data


main = Blueprint('main', __name__)

@main.route('/api/stock', methods=['POST'])
def get_stock_data():
    # TODO: add a check here to look at what data we already have in 
    # sqlite, if we need to grab new data from yf do it, if not
    # just pull from db.
    data = request.json
    symbol = data.get('symbol')
    period = data.get('period', '1mo')
    try:
        stock_data = get_preprocess_store_data(symbol, period)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    # Convert to JSON for front end display
    result = stock_data.to_dict(orient='records')
    return jsonify(result)