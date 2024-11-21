import React from "react";
import { useParams, Link } from "react-router-dom";

const movies = [
  { id: 1, title: "Inception", description: "A mind-bending thriller." },
  { id: 2, title: "The Dark Knight", description: "A heroic tale." },
  { id: 3, title: "Interstellar", description: "A journey to the stars." },
];

const MovieDetails = () => {
  const { id } = useParams();
  const movie = movies.find((movie) => movie.id === parseInt(id));

  if (!movie) {
    return <h2>Movie not found</h2>;
  }

  return (
    <div>
      <h1>{movie.title}</h1>
      <p>{movie.description}</p>
      <Link to={`/reserve/${movie.id}`}>Reserve Tickets</Link>
      <br />
      <Link to="/">Back to Movies</Link>
    </div>
  );
};

export default MovieDetails;
