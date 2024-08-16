import React from 'react';

function Results({ data }) {
    return (
        <div className="results">
            <h2>Stock Data</h2>
            <Plot data={data} xKey="Date" yKey="Close" title="Closing Prices" />
            <Plot data={data} xKey="Date" yKey="rolling_mean_5" title="5-Day Rolling Mean" />
            <Plot data={data} xKey="Date" yKey="rolling_std_5" title="5-Day Rolling Std Dev" />
        </div>
    );
}

export default Results;