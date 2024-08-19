# candelabra
visually driven stock analysis powered by live data and machine learning

## Organization
```
candelabra/
│
├── backend/                      # Flask backend
│   ├── app/                      # Flask application package
│   │   ├── __init__.py           # Initialize Flask app and routes
│   │   ├── routes.py             # Define API routes
│   │   ├── arima_model.py        # ARIMA predictive ML model
        ├── databases.py          # Define local databases (SQLite)
│   │   └── data_processing.py    # Data gathering & preprocessing funcs
│   ├── venv/                     # Virtual environment (optional)
│   ├── run.py                    # Entry point to run the Flask app
│   └── requirements.txt          # Python dependencies
│
├── frontend/                     # React frontend
│   ├── public/                   # Static files (HTML, etc.)
│   ├── src/                      # React source files
│   │   ├── components/           # Reusable React components
│   │   │   ├── App.js            # Main React component
│   │   │   ├── StockInput.js     # Component for inputting stock symbol
│   │   │   ├── Results.js        # Component to display/plot results
            ├── ARIMAPredictor.js # Component to display model results
|   |   |   └── Plot.js           # Component to define plot
│   │   ├── App.css               # Styles for React components
│   │   └── index.js              # Entry point for React
│   ├── package.json              # Node dependencies
│   └── package-lock.json         # Locked versions of dependencies
│
└── README.md                     # Project overview and setup instructs
```

## Philosophy 

- **Separation of Concerns**: Keep the backend and frontend code separate to maintain a clear structure and make the project easier to manage.
- **Modular Code**: Break down code into small, reusable functions and components, making it easier to test and maintain.
- **Version Control**: Use Git to track changes and collaborate effectively.
- **Environment Management**: Use virtual environments for Python and Node modules to avoid dependency conflicts.
- **API-First Design**: Develop the backend API with clear endpoints that the frontend can consume.