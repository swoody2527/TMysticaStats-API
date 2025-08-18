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
    print(response.get_json())

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
        