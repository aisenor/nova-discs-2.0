// frontend/src/pages/home.js
import React, { useState, useEffect } from 'react';

const Home = () => {
  const [data, setData] = useState({});

  useEffect(() => {
    fetch('http://localhost:8000/scorecard/')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h1>{data.message}</h1>
    </div>
  );
};

export default Home;