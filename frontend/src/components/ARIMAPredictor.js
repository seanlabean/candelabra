import React, { useState } from 'react';

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