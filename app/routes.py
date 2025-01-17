from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Movie, Booking

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/movies')
def view_movies():
    movies = Movie.query.all()
    return render_template("movies.html", movies=movies)

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        time = request.form['time']
        movie = Movie(title=title, description=description, time=time)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('view_movies'))
    return render_template("add_movie.html")

@app.route('/bookings')
def view_bookings():
    bookings = Booking.query.all()
    return render_template("bookings.html", bookings=bookings)

@app.route('/edit_movie/<int:movie_id>', methods=['GET', 'POST'])
def edit_movie(movie_id):
    movie = db.session.get(Movie, movie_id)  # Poprawka: przypisanie wyniku do `movie`
    if not movie:
        return redirect(url_for('view_movies'))  # Obsługa przypadku, gdy film nie istnieje
    if request.method == 'POST':
        movie.title = request.form['title']
        movie.description = request.form['description']
        movie.time = request.form['time']
        db.session.commit()
        return redirect(url_for('view_movies'))
    return render_template('edit_movie.html', movie=movie)

@app.route('/delete_movie/<int:movie_id>', methods=['GET'])
def delete_movie(movie_id):
    movie = db.session.get(Movie, movie_id)
    if movie:  # Dodanie sprawdzania, czy film istnieje
        db.session.delete(movie)
        db.session.commit()
    return redirect(url_for('view_movies'))

@app.route('/delete_booking/<int:booking_id>', methods=['GET'])
def delete_booking(booking_id):
    booking = db.session.get(Booking, booking_id)  # Poprawka: przypisanie wyniku do `booking`
    if booking:  # Dodanie sprawdzania, czy rezerwacja istnieje
        db.session.delete(booking)
        db.session.commit()
    return redirect(url_for('view_bookings'))

@app.route('/booking/<int:movie_id>', methods=['GET', 'POST'])
def booking(movie_id):
    movie = db.session.get(Movie, movie_id)  # Poprawka: użycie `db.session.get`
    if not movie:
        return redirect(url_for('view_movies'))  # Obsługa przypadku, gdy film nie istnieje
    if request.method == 'POST':
        name = request.form['name']
        tickets = request.form['tickets']
        booking = Booking(name=name, tickets=tickets, movie_id=movie.id)
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for('view_bookings'))
    return render_template('booking.html', movie=movie)

@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

@app.route('/book/<int:movie_id>', methods=['GET'])
def book_movie(movie_id):
    movie = db.session.get(Movie, movie_id)  
    if not movie:
        return redirect(url_for('view_movies')) 
    return render_template('book.html', movie=movie)

