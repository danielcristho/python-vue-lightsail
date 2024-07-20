import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Pong!'}

def test_get_book(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert 'books' in response.get_json()

def test_post_book(client):
    data = {
        'title': 'Test Book',
        'author': 'Test Author',
        'read': True
    }
    response = client.post('/books', json=data)
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Book added!'

    response = client.get('/books')
    books = response.get_json()['books']
    assert any(book['title'] == 'Test Book' for book in books)
