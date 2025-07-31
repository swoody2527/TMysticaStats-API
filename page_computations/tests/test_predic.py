from urllib.parse import urlencode


def test_prediction(client):
    #num_players, map_id, f_tiles, b_tiles, t_tiles, s_tiles, g_factions
    num_players = 4
    map_id = '126fe960806d587c78546b30f1a90853b1ada468'.upper()
    b_tiles = ['BON2','BON3','BON1', 'BON4', 'BON8', 'BON5']
    factions = ['DARKLINGS', 'DWARVES', 'AUREN', 'CHAOSMAGICIANS']
    score_tiles = ['SCORE2', 'SCORE3', 'SCORE8', 'SCORE7', 'SCORE4', 'SCORE5']

    params = [
    ('factions_included', 'True'),
    ('num_players', num_players),
    ('map_id', map_id),
] + [('bonus_tiles', b) for b in b_tiles] \
  + [('score_tiles', s) for s in score_tiles] \
  + [('game_factions', f) for f in factions]

    query = urlencode(params)
    request_string = f'/api/predictions/vp_prediction?{query}'
    response = client.get(request_string)

    assert response.status_code == 200



def test_prediction_class(client):
    #num_players, map_id, f_tiles, b_tiles, t_tiles, s_tiles, g_factions
    num_players = 4
    map_id = '126fe960806d587c78546b30f1a90853b1ada468'.upper()
    b_tiles = ['BON2','BON3','BON1', 'BON4', 'BON8', 'BON5']
    factions = ['DARKLINGS', 'DWARVES', 'AUREN', 'CHAOSMAGICIANS']
    score_tiles = ['SCORE2', 'SCORE3', 'SCORE8', 'SCORE7', 'SCORE4', 'SCORE5']

    params = [
    ('factions_included', 'True'),
    ('num_players', num_players),
    ('map_id', map_id),
] + [('bonus_tiles', b) for b in b_tiles] \
  + [('score_tiles', s) for s in score_tiles] \
  + [('game_factions', f) for f in factions]

    query = urlencode(params)
    request_string = f'/api/predictions/win_prediction?{query}'
    response = client.get(request_string)

    assert response.status_code == 200



def test_prediction_class_no_faction(client):
    #num_players, map_id, f_tiles, b_tiles, t_tiles, s_tiles, g_factions
    num_players = 4
    map_id = '126fe960806d587c78546b30f1a90853b1ada468'.upper()
    b_tiles = ['BON2','BON3','BON1', 'BON4', 'BON8', 'BON5']
    factions = []
    score_tiles = ['SCORE2', 'SCORE3', 'SCORE8', 'SCORE7', 'SCORE4', 'SCORE5']

    params = [
        ('factions_included', 'False'),
        ('num_players', num_players),
        ('map_id', map_id),
    ] + [('bonus_tiles', b) for b in b_tiles] \
    + [('score_tiles', s) for s in score_tiles] \
    + [('game_factions', f) for f in factions]

    query = urlencode(params)
    request_string = f'/api/predictions/win_prediction?{query}'
    response = client.get(request_string)

    assert response.status_code == 200
        

def test_invalid_num_players_type(client):
    params = [
        ('factions_included', 'True'),
        ('num_players', 'four'),
        ('map_id', '126FE960806D587C78546B30F1A90853B1ADA468'),
        ('bonus_tiles', 'BON1'),
        ('score_tiles', 'SCORE1'),
        ('game_factions', 'auren')
    ]
    query = urlencode(params)
    response = client.get(f'/api/predictions/win_prediction?{query}')
    assert response.status_code == 400
    assert b'Invalid type for No. Players' in response.data


def test_missing_map_id(client):
    params = [
        ('factions_included', 'True'),
        ('num_players', 4),
        ('bonus_tiles', 'BON1'),
        ('score_tiles', 'SCORE1'),
        ('game_factions', 'auren')
    ]
    query = urlencode(params)
    response = client.get(f'/api/predictions/win_prediction?{query}')
    assert response.status_code == 400
    assert b'Missing player number or map parameter' in response.data


def test_invalid_map_id(client):
    params = [
        ('factions_included', 'True'),
        ('num_players', 4),
        ('map_id', 'INVALIDMAP'),
        ('bonus_tiles', 'BON1'),
        ('score_tiles', 'SCORE1'),
        ('game_factions', 'auren')
    ]
    query = urlencode(params)
    response = client.get(f'/api/predictions/win_prediction?{query}')
    assert response.status_code == 400
    assert b'Invalid map id' in response.data


def test_invalid_faction_name(client):
    params = [
        ('factions_included', 'True'),
        ('num_players', 4),
        ('map_id', '126FE960806D587C78546B30F1A90853B1ADA468'),
        ('bonus_tiles', 'BON1'),
        ('score_tiles', 'SCORE1'),
        ('game_factions', 'invalidfaction')
    ]
    query = urlencode(params)
    response = client.get(f'/api/predictions/win_prediction?{query}')
    assert response.status_code == 400
    assert b'Invalid faction choice' in response.data


def test_factions_flag_true_but_no_factions(client):
    params = [
        ('factions_included', 'True'),
        ('num_players', 4),
        ('map_id', '126FE960806D587C78546B30F1A90853B1ADA468'),
        ('bonus_tiles', 'BON1'),
        ('score_tiles', 'SCORE1')
    ]
    query = urlencode(params)
    response = client.get(f'/api/predictions/win_prediction?{query}')
    assert response.status_code == 400
    assert b'enemy faction data but none was provided' in response.data.lower()


def test_num_players_out_of_bounds(client):
    params = [
        ('factions_included', 'False'),
        ('num_players', 6), 
        ('map_id', '126FE960806D587C78546B30F1A90853B1ADA468'),
        ('bonus_tiles', 'BON1'),
        ('score_tiles', 'SCORE1')
    ]
    query = urlencode(params)
    response = client.get(f'/api/predictions/win_prediction?{query}')
    assert response.status_code == 400
    assert b'No. players must be between 2 and 5' in response.data


def test_missing_bonus_tiles(client):
    params = [
        ('factions_included', 'False'),
        ('num_players', 4),
        ('map_id', '126FE960806D587C78546B30F1A90853B1ADA468'),
        ('score_tiles', 'SCORE1')
    ]
    query = urlencode(params)
    response = client.get(f'/api/predictions/win_prediction?{query}')
    assert response.status_code == 400
    assert b'Missing bonus/scoring tile information' in response.data


def test_missing_score_tiles(client):
    params = [
        ('factions_included', 'False'),
        ('num_players', 4),
        ('map_id', '126FE960806D587C78546B30F1A90853B1ADA468'),
        ('bonus_tiles', 'BON1')
    ]
    query = urlencode(params)
    response = client.get(f'/api/predictions/win_prediction?{query}')
    assert response.status_code == 400
    assert b'Missing bonus/scoring tile information' in response.data