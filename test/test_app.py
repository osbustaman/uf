import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_uf(client):
    response = client.get('/get-uf/28/04/2023')
    data = response.get_json()

    assert response.status_code == 200
    assert data['fecha'] == '28-04-2023'
    assert data['valor_actual'] is not None

def test_get_uf_invalid_date(client):
    response = client.get('/get-uf/31/02/2023')
    data = response.get_json()

    assert response.status_code == 200
    assert data['accion'] == 'error'
    assert data['mensaje'] == 'La fecha ingresada no es válida'

def test_get_uf_before_min_date(client):
    response = client.get('/get-uf/01/01/2010')
    data = response.get_json()

    assert response.status_code == 200
    assert data['accion'] == 'error'
    assert data['mensaje'] == 'La fecha ingresada debe ser mayor a 01-01-2013'
