import React, { useState } from 'react'

/**
 * StockInput component allows users to input a stock symbol and submit it for data fetching.
 *
 * @component
 * @param {Object} props - The component props.
 * @param {Function} props.onSubmit - A callback function that is triggered when the form is submitted with a valid stock symbol.
 * @example
 * return (
 *   <StockInput onSubmit={handleStockFetch} />
 * )
 *
 * @returns {JSX.Element} A form with an input field for entering the stock symbol and a submit button.
 *
 * @description
 * - Users can type in a stock symbol into the input field.
 * - Upon submitting the form, the `onSubmit` function is called with the stock symbol as an argument, provided that the input is not empty.
 * - Prevents the default form submission behavior to handle the submission asynchronously.
 */
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