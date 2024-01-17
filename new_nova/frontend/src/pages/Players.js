// frontend/src/pages/players.js
import React, { useState, useEffect } from 'react';

import PlayersTemplate from './templates/PlayersTemplate';

const Players = () => {
  const [data, setData] = useState({});

  useEffect(() => {
    fetch('http://localhost:8000/players/')
      .then(response => response.json())
      .then(data => {
        const parsedPlayers = JSON.parse(data.players);
        setData({ players: parsedPlayers });
      })
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
      <PlayersTemplate data={data} />
  );
};

export default Players;

