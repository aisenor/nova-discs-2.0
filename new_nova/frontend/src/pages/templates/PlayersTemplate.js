import React, { useState } from 'react';
import { FaArrowUp, FaArrowDown } from 'react-icons/fa';

import './generic.css';

const PlayersTemplate = ({ data }) => {


  const [sortColumn, setSortColumn] = useState(null);
  const [sortOrder, setSortOrder] = useState('asc');
  if (!data || !data.players || !Array.isArray(data.players)) {
    // Handle the case where data is not available or in the expected format
    return <div className="page">Loading ... </div>;
  }
  const handleHeaderClick = (column) => {
    if (sortColumn === column) {
      setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc');
    } else {
      setSortColumn(column);
      setSortOrder('asc');
    }
  };

  const sortedPlayers = [...data.players].sort((a, b) => {
    let aValue = a[sortColumn];
    let bValue = b[sortColumn];

    // Handle undefined values
    if (aValue === undefined) aValue = '';
    if (bValue === undefined) bValue = '';

    // Use the default comparison for strings and numbers
    if (sortOrder === 'asc') {
      return aValue < bValue ? -1 : aValue > bValue ? 1 : 0;
    } else {
      return bValue < aValue ? -1 : bValue > aValue ? 1 : 0;
    }
  });

  return (
    <div className="page">
      <table className="styled-table">
        <thead>
          <tr>
            <th onClick={() => handleHeaderClick('id')}>
              ID {sortColumn === 'id' && (sortOrder === 'asc' ? <FaArrowUp /> : <FaArrowDown />)}
            </th>
            <th onClick={() => handleHeaderClick('name')}>
              Name {sortColumn === 'name' && (sortOrder === 'asc' ? <FaArrowUp /> : <FaArrowDown />)}
            </th>
          </tr>
        </thead>
        <tbody>
          {sortedPlayers.map((player) => (
            <tr key={player.id}>
              <td>{player.id}</td>
              <td>{player.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default PlayersTemplate;
