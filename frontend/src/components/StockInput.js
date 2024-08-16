import React, { useState } from 'react'

function StockInput({ onSubmit }) {
    const [symbol, setSymbol] = useState('');
    const handleSubmit = (e) => {
        e.preventDefault();
        if (symbol) onSubmit(symbol);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input 
                type="text"
                value={symbol}
                onChange={(e) => setSymbol(e.target.value)}
                placeholder="Enter Stock Symbol"
            />
            <button type="submit">Get Data</button>
        </form>
    );
}

export default StockInput;