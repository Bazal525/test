import pytest
from app import app, db
from app.models import Movie

@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_index_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Witamy' in response.data

def test_add_movie_page(test_client):
    response = test_client.get('/add_movie')
    assert response.status_code == 200
    assert b'Dodaj nowy film' in response.data

def test_movies_list_page(test_client):
    with app.app_context():
        movie = Movie(title='List Movie', description='Description', time='21:00')
        db.session.add(movie)
        db.session.commit()
    response = test_client.get('/movies')
    assert response.status_code == 200
    assert b'List Movie' in response.data

def test_edit_movie_page(test_client):
    with app.app_context():
        movie = Movie(title='Edit Test', description='Old Desc', time='20:00')
        db.session.add(movie)
        db.session.commit()
        movie_id = movie.id
    response = test_client.get(f'/edit_movie/{movie_id}')
    assert response.status_code == 200
    assert b'Edit Test' in response.data

def test_booking_page(test_client):
    with app.app_context():
        movie = Movie(title='Booking Test', description='Desc', time='20:00')
        db.session.add(movie)
        db.session.commit()
        movie_id = movie.id
    response = test_client.get(f'/booking/{movie_id}')
    assert response.status_code == 200
    assert b'Booking Test' in response.data

def test_delete_movie_page(test_client):
    with app.app_context():
        movie = Movie(title='Delete Test', description='Description', time='20:00')
        db.session.add(movie)
        db.session.commit()
        movie_id = movie.id
    response = test_client.get(f'/delete_movie/{movie_id}', follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        assert db.session.query(Movie).filter_by(id=movie_id).first() is None

def test_invalid_movie(test_client):
    response = test_client.get('/movie/999', follow_redirects=True)
    assert response.status_code == 404

def test_404_page(test_client):
    response = test_client.get('/invalid')
    assert response.status_code == 404
    assert b'Strona nie znaleziona' in response.data

def test_home_links(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Zobacz filmy' in response.data
    assert b'Dodaj nowy film' in response.data

def test_index_contains_links(test_client):
    """
    Test sprawdzający, czy strona główna zawiera linki do listy filmów
    i dodawania nowego filmu.
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Zobacz filmy' in response.data
    assert b'Dodaj nowy film' in response.data


