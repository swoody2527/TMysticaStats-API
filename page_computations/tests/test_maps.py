from app import app

'''INPUT VALIDATION TESTS'''

def test_valid_inputs(client):
    response = client.get('/api/maps/games-per-map?map_id=be8f6ebf549404d015547152d5f2a1906ae8dd90&' \
    's_year=2013&e_year=2014')

    assert response.status_code == 200


def test_invalid_map_id(client):
    response = client.get('/api/maps/games-per-map?map_id=INVALID&' \
    's_year=2013&e_year=2014')

    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Invalid map id.'

def test_missing_param(client):
    response = client.get('/api/maps/games-per-map?' \
    's_year=2013&e_year=2014')

    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Missing 1 or more parameters for search.'

def test_invalid_year(client):
     response = client.get('/api/maps/games-per-map?map_id=be8f6ebf549404d015547152d5f2a1906ae8dd90&' \
    's_year=2013&e_year=2035')
     
     assert response.status_code == 400
     data = response.get_json()
     assert data['error'] == 'Parameter out of bounds.'





    
def test_player_map_dist(client):
    response = client.get('/api/maps/avg-players-per-map?map_id=be8f6ebf549404d015547152d5f2a1906ae8dd90&' \
    's_year=2013&e_year=2014')

    assert response.status_code == 200

def test_player_map_pickrate(client):
    response = client.get('/api/maps/faction-pickrate?map_id=be8f6ebf549404d015547152d5f2a1906ae8dd90&' \
    's_year=2013&e_year=2014')

    assert response.status_code == 200

def test_player_map_pickrate(client):
    response = client.get('/api/maps/faction-winrate?map_id=be8f6ebf549404d015547152d5f2a1906ae8dd90&' \
    's_year=2013&e_year=2014')

    assert response.status_code == 200
