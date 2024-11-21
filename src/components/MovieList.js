import React from "react";
import { Link } from "react-router-dom";

const movies = [
  { id: 1, title: "Inception", description: "A mind-bending thriller." },
  { id: 2, title: "The Dark Knight", description: "A heroic tale." },
  { id: 3, title: "Interstellar", description: "A journey to the stars." },
];

const MovieList = () => {
  return (
    <div>
      <h1>Movies</h1>
      <ul>
        {movies.map((movie) => (
          <li key={movie.id}>
            <Link to={`/movie/${movie.id}`}>
              <strong>{movie.title}</strong>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MovieList;
