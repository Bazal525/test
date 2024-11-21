import React, { useState } from "react";
import { useParams, Link } from "react-router-dom";

const Reservation = () => {
  const { id } = useParams();
  const [name, setName] = useState("");
  const [seats, setSeats] = useState(1);
  const [confirmation, setConfirmation] = useState(false);

  const handleReservation = (e) => {
    e.preventDefault();
    setConfirmation(true);
  };

  return (
    <div>
      <h1>Reserve Tickets for Movie #{id}</h1>
      {confirmation ? (
        <p>
          Thank you, {name}! You have reserved {seats} seat(s).
        </p>
      ) : (
        <form onSubmit={handleReservation}>
          <label>
            Name:
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            />
          </label>
          <br />
          <label>
            Number of Seats:
            <input
              type="number"
              value={seats}
              min="1"
              onChange={(e) => setSeats(e.target.value)}
              required
            />
          </label>
          <br />
          <button type="submit">Reserve</button>
        </form>
      )}
      <Link to="/">Back to Movies</Link>
    </div>
  );
};

export default Reservation;
