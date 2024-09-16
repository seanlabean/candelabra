import React, { useState } from 'react';
import StockInput from './StockInput';
import Results from './Results';
import ARIMAPredictor from './ARIMAPredictor';
import '../App.css';

/**
 * App component is the main entry point for the stock prediction app.
 *
 * @component
 * @example
 * return (
 *   <App />
 * )
 *
 * @returns {JSX.Element} The main application component which includes a stock input form, ARIMA predictions, and results display.
 *
 * @description
 * - Displays the application title and integrates multiple components: `StockInput`, `ARIMAPredictor`, and `Results`.
 * - Handles fetching stock data based on the symbol entered by the user.
 * - The fetched data is passed to the `Results` component for display.
 */
function App() {
  const [results, setResults] = useState(null);

  const fetchData = async (symbol) => {
    const response = await fetch('/api/stock', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ symbol })
    });
    const data = await response.json();
    setResults(data);
  };

  return (
    <div className="App">
        <h1>🕯️candelabra🕯️</h1>
        <StockInput onSubmit={fetchData} />
        <ARIMAPredictor />
        {results && <Results data={results} />}
    </div>
  );
}

export default App;
