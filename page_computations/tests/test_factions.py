
# TEST DATA RUNS FROM 2013 - 2014

"""WINRATES TESTS"""

def test_winrates(client):
    response = client.get('api/factions/faction-wr?' 
    'faction=dwarves&s_year=2013&e_year=2014&num_players=3')
    
    assert response.status_code == 200

    data = response.get_json()
    
    assert data['faction'] == 'dwarves'
    assert data['winrate'] == 27.34
    assert data['total_games'] == 395
    assert data['total_wins'] == 108

def test_winrates_missing_param(client):
    response = client.get('api/factions/faction-wr?' 
    'faction=dwarves&s_year=2013&num_players=3')

    assert response.status_code == 400
    data = response.get_json()

    assert data['error'] == 'Missing 1 or more parameters for search.'

def test_winrates_invalid_type(client):

    response = client.get('api/factions/faction-wr?' 
    'faction=dwarves&s_year=2013&e_year=2014&num_players=INVALID')

    assert response.status_code == 400
    data = response.get_json()

    assert data['error'] == '1 or more invalid parameter type(s).'

def test_winrates_oob(client):
    response = client.get('api/factions/faction-wr?' 
    'faction=dwarves&s_year=2013&e_year=2014&num_players=1000')

    assert response.status_code == 400

    data = response.get_json()

    assert data['error'] == 'Player number filter out of bounds.'

def test_num_player_ommited(client):
    response = client.get('api/factions/faction-wr?' 
    'faction=dwarves&s_year=2013&e_year=2014')

    assert response.status_code == 200
    data = response.get_json()

    assert data['faction'] == 'dwarves'
    assert data['total_games'] == 2068


def test_valid_faction(client):
    response = client.get('api/factions/faction-wr?' 
    'faction=INVALID&s_year=2013&e_year=2014')

    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Invalid faction choice.'

def test_faction_omitted(client):
    response = client.get('api/factions/faction-wr?' 
    's_year=2013&e_year=2014&num_players=3')

    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Faction required for search.'








def test_pickrates(client):
    # Pickrates uses same input validation as winrates (above)
    # so safety is assumed here.
    
    
    response = client.get('api/factions/faction-pickrate?' 
    'faction=dwarves&s_year=2013&e_year=2014&num_players=3')

    assert response.status_code == 200

    data = response.get_json()

    assert data['faction'] == 'dwarves'
    assert data['pickrate'] == 16.38
    assert data['picked_games'] == 395
    assert data['total_games'] == 2412

def test_wr_versus(client):
    response = client.get('api/factions/faction-wr-versus?faction=dwarves&s_year=2013&' \
    'e_year=2014&num_players=3')

    assert response.status_code == 200

    data = response.get_json()

    assert 'dwarves' not in data.keys()
    assert data['darklings']['win_rate'] == 25.98
    assert data['darklings']['games_together'] == 127


def test_wr_by_map(client):
    response = client.get('api/factions/faction-wr-maps?faction=dwarves&s_year=2013&' \
    'e_year=2014&num_players=3')

    assert response.status_code == 200

    data = response.get_json()
    
    for map_code, values in data.items():
        assert values['total_games'] > 0

def test_faction_vp(client):
    response = client.get('api/factions/faction-avg-vp?faction=dwarves&s_year=2013&'
    'e_year=2014')

    assert response.status_code == 200


def test_vp_by_round(client):
    response = client.get('api/factions/faction-avg-vp-per-round?faction=dwarves&s_year=2013&'
    'e_year=2014')

    assert response.status_code == 200


def test_games_played(client):
    response = client.get('api/factions/faction-games-played?faction=dwarves&s_year=2013&'
    'e_year=2014')

    assert response.status_code == 200


def test_games_played(client):
    response = client.get('api/factions/faction-games-played?faction=dwarves&s_year=2013&'
    'e_year=2014')

    assert response.status_code == 200

def test_wr_playercount(client):
    response = client.get('api/factions/wr-by-playercount?faction=dwarves&s_year=2013&'
    'e_year=2014')

    assert response.status_code == 200