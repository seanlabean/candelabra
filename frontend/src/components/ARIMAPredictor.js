import React, { useState } from 'react';

/**
 * ARIMAPredictor component allows users to enter a stock symbol and fetch ARIMA model predictions.
 *
 * @component
 * @example
 * return (
 *   <ARIMAPredictor />
 * )
 *
 * @returns {JSX.Element} A component with an input field for the stock symbol and a button to request ARIMA predictions.
 *
 * @description
 * - Users can input a stock symbol into a text field.
 * - Upon clicking the "Predict" button, the component sends a POST request to an API endpoint `/api/predict_arima` with the stock symbol and a fixed step value of 5.
 * - The fetched ARIMA predictions are displayed as a list, showing predictions for the next 5 days.
 */
const ARIMAPredictor = () => {
    const [symbol, setSymbol] = useState('');
    const [predictions, setPredictions] = useState([]);

    const handlePredict = async () => {
        const response = await fetch('/api/predict_arima', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ symbol, steps: 5 })
        });
        const data = await response.json();
        setPredictions(data.predictions);
    };

    return (
        <div>
            <input 
                type="text" 
                value={symbol} 
                onChange={(e) => setSymbol(e.target.value)} 
                placeholder="Enter stock symbol" 
            />
            <button onClick={handlePredict}>Predict</button>
            <div>
                {predictions.length > 0 && (
                    <ul>
                        {predictions.map((pred, index) => (
                            <li key={index}>Day {index + 1}: {pred}</li>
                        ))}
                    </ul>
                )}
            </div>
        </div>
    );
};

export default ARIMAPredictor;