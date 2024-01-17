import React, { useState } from 'react';

import './Scorecard.css'

const ScorecardTemplate = () => {
  const [formData, setFormData] = useState({
    date: '',
    player: '',
    score: '',
  });

  const [error, setError] = useState(null); // State variable for tracking errors

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:8000/putting_league/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        console.log('Score posted successfully');
        // You can redirect or perform any other action after successful submission
      } else {
        const responseData = await response.json()

        if (responseData.player && responseData.player.length > 0) {
          setError(`Invalid PDGA ID. You aren't setup for putting league.`);
        } else {
          console.error('Failed to post score');
          setError('Failed to post score. Please try again.');
        }
      }
    } catch (error) {
      console.error('Error posting score', error);
      setError('Error posting score. Please try again.'); // Set error message
    }
  };

  return (
    <div>
      {error && <p className="error-banner">{error}</p>}
      <form onSubmit={handleSubmit}>
        <label>Date: </label>
        <input
          type="date"
          name="date"
          value={formData.date}
          onChange={handleChange}
          required
        />
        <br />

        <label>PDGA #: </label>
        <input
          type="text"
          name="player"
          value={formData.player}
          onChange={handleChange}
          required
        />
        <br />
        <label>Score: </label>
        <input
          type="number"
          name="score"
          value={formData.score}
          onChange={handleChange}
          required
        />

        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default ScorecardTemplate;
