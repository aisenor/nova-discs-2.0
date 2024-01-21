import React, { useState, useEffect } from 'react';

const StandingsTemplate = ({ data }) => {

  const renderDayTable = (date, playerScores) => (
    <div key={date}>
      <h2>{date}</h2>
      <table className="styled-table">
        <thead>
          <tr>
            <th>Player</th>
            <th>Total Score</th>
          </tr>
        </thead>
        <tbody>
          {playerScores.map(([playerID, score]) => (
            <tr key={playerID}>
              <td>{playerID}</td>
              <td>{score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );

  const renderTop5Table = (top5Players) => (
    <div>
      <h2>Top 5 Players</h2>
      <table className="styled-table">
        <thead>
          <tr>
            <th>Player</th>
            <th>Total Score</th>
          </tr>
        </thead>
        <tbody>
          {top5Players.map(([playerID, score]) => (
            <tr key={playerID}>
              <td>{playerID}</td>
              <td>{score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );

  return (
    <div>
      {data && data.top_3_daily && data.top_5 ? (
        <>
          {renderTop5Table(data.top_5)}

          {Object.entries(data.top_3_daily).map(([date, playerScores]) =>
            renderDayTable(date, playerScores)
          )}

        </>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default StandingsTemplate;
