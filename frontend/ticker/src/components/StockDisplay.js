import React, {useEffect, useState} from "react";

function StockDisplay() {
    const [data, setData] = useState([]);
    // const [page, setPage] = useState(1);

    useEffect(() => {
      fetch(`http://localhost:8000/data/all?page=0`)
        .then(response => response.json())
        .then(data => setData(data));
    }, []);

    return (
        <table className="table table-bordered">
          <thead>
            <tr>
              <th>DateTime</th>
              <th>Open</th>
              <th>Close</th>
              <th>High</th>
              <th>Low</th>
              <th>Instrument</th>
            </tr>
          </thead>
          <tbody>
            {data.map(item => (
              <tr key={item.id}>
                <td>{item.date}</td>
                <td>{item.open}</td>
                <td>{item.close}</td>
                <td>{item.high}</td>
                <td>{item.low}</td>
                <td>{item.instrument}</td>
              </tr>
            ))}
          </tbody>
        </table>
      );
}

export default StockDisplay