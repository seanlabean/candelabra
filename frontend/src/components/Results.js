import React from 'react';
import Plot from './Plot';

/**
 * Results component displays the stock data by rendering a plot of closing prices.
 *
 * @component
 * @param {Object} props - The component props.
 * @param {Array} props.data - The stock data to be plotted, where each object represents a stock data point.
 * @example
 * const stockData = [{ Date: '2024-09-01', Close: 123.45 }, { Date: '2024-09-02', Close: 127.89 }];
 * return (
 *   <Results data={stockData} />
 * )
 *
 * @returns {JSX.Element} A div containing the stock data plot.
 *
 * @description
 * - The `Results` component receives an array of stock data as a prop.
 * - It displays a plot of the closing prices, using the `Plot` component.
 * - The plot uses "Date" as the x-axis key and "Close" as the y-axis key.
 */
function Results({ data }) {
    const yKs = ["Close"];
    return (
        <div className="results">
            <h2>Stock Data</h2>
            <Plot data={data} xKey="Date" yKeys={yKs} title="Closing Prices" />
        </div>
    );
}

export default Results;