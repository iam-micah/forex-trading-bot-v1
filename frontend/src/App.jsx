import "./App.css";
import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
    const [oandaData, setOandaData] = useState(null);

    useEffect(() => {
        axios
            .get("http://localhost:5000/oanda-data")
            .then((response) => {
                setOandaData(response.data);
            })
            .catch((error) => console.error("Error fetching data: ", error));
    }, []);
    return (
        <div>
            {oandaData ? (
                <div>{JSON.stringify(oandaData)}</div>
            ) : (
                <p>Loading...</p>
            )}
        </div>
        // <div>
        //     <p>Hello</p>
        // </div>
    );
}

export default App;
