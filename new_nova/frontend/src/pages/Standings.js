// frontend/src/pages/home.js
import React, { useState, useEffect } from 'react';

import StandingsTemplate from './templates/StandingsTemplate';

const Home = () => {
  const [data, setData] = useState({});

  useEffect(() => {
    fetch('http://localhost:8000/standings/')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
    console.log(data)
  }, []);

  return (
      <StandingsTemplate data={data} />

    // <div>
    //   <pre>{JSON.stringify(data, null, 2)}</pre>
    // </div>
  );
};

export default Home;
