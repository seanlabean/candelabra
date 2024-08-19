from . import db

class StockData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    open = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    lag_1 = db.Column(db.Float)
    lag_2 = db.Column(db.Float)
    lag_3 = db.Column(db.Float)
    lag_4 = db.Column(db.Float)
    lag_5 = db.Column(db.Float)
    rolling_mean_5 = db.Column(db.Float)
    rolling_std_5 = db.Column(db.Float)

