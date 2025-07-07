import pytest
from app import app


"""WINRATES TESTS"""

def test_winrates(client):
    response = client.get('api/factions/faction-wr?' 
    'faction=dwarves&s_year=2017&e_year=2020&num_players=3')
    
    assert response.status_code == 200

    data = response.get_json()
    
    assert data['faction'] == 'dwarves'
    assert data['winrate'] == 27.01
    assert data['total_games'] == 1018
    assert data['total_wins'] == 275

def test_winrates_missing_param(client):
    response = client.get('api/factions/faction-wr?' 
    'faction=dwarves&s_year=2017&e_year=2020')

    assert response.status_code == 400
    data = response.get_json()

    assert data['error'] == 'Missing 1 or more parameters for search.'

def test_winrates_invalid_type(client):

    response = client.get('api/factions/faction-wr?' 
    'faction=dwarves&s_year=2017&e_year=2020&num_players=INVALID')

    assert response.status_code == 400
    data = response.get_json()

    assert data['error'] == '1 or more invalid parameter type(s).'

def test_winrates_oob(client):
    response = client.get('api/factions/faction-wr?' 
    'faction=dwarves&s_year=2017&e_year=2020&num_players=1000')

    assert response.status_code == 400

    data = response.get_json()

    assert data['error'] == 'Parameter out of bounds.'




"""PICK RATES TESTS"""

def test_pickrates(client):
    pass
