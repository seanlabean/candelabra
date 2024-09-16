import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function Plot({ data, xKey, yKeys, title }) {
    const formatYAxis = (tick) => tick.toFixed(2);
    return (
        <div>
            <h3>{title}</h3>
            <ResponsiveContainer width="100%" height={300}>
                <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey={xKey} />
                    <YAxis domain={['dataMin', 'dataMax']} tickFormatter={formatYAxis}/>
                    <Tooltip />
                    <Legend />
                    {yKeys.map((yKey, index) => (
                        <Line
                            key={index}
                            type="monotone"
                            dataKey={yKey}
                            stroke={yKey.color}
                            activeDot={{ r: 8 }}
                        />
                    ))}
                </LineChart>
            </ResponsiveContainer>
        </div>
    );
}

export default Plot;