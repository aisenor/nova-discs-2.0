import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <React.StrictMode>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
            <title>Your React App Title</title>
        </head>
        <App/>
    </React.StrictMode>
);

reportWebVitals();