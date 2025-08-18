from ..utils import validate_pred_inputs as val

test_player = 4
test_map = '126FE960806D587C78546B30F1A90853B1ADA468'
test_s_tiles = [f'SCORE{i+1}' for i in range(6)]
test_b_tiles = [f'BON{i+1}' for i in range(7)]

def test_missing_map_players():
    err, res = val.validate_model_inputs(None, None, None, test_b_tiles, test_s_tiles, None)

    assert res is None
    assert err == 'Missing player number or map parameter.'

def test_missing_tiles():
    err, res = val.validate_model_inputs(None, test_player, test_map, [], [], None)

    assert res is None
    assert err == 'Missing bonus/scoring tile information.'

def test_invalid_num_player_type():
    err, res = val.validate_model_inputs(None, 'INVALID STRING', test_map, test_s_tiles, test_b_tiles, None)
    
    assert res is None
    assert err == 'Invalid type for No. Players'

def test_num_players_oob():
    err, res = val.validate_model_inputs(None, 10, test_map, test_s_tiles, test_b_tiles, None)

    assert res is None
    assert err == 'Cannot make predictions. No. players must be between 2 and 5'

def test_invalid_map():
    err, res = val.validate_model_inputs(None, test_player, 'INVALID MAP', test_b_tiles, test_s_tiles, None)

    assert res is None
    assert err == 'Invalid map id.'

def test_invalid_b_tile():
    err, res = val.validate_model_inputs(None, test_player, test_map, ['INVALID B TILE'], test_s_tiles, None)

    assert res is None
    assert err == 'Invalid bonus tile.'

def test_invalid_s_tile():
    err, res = val.validate_model_inputs(None, test_player, test_map, test_b_tiles, ['INVALID S TILE'], None)

    assert res is None
    assert err == 'Invalid score tile.'

def test_happy_path():
    err, res = val.validate_model_inputs(None, test_player, test_map, test_b_tiles, test_s_tiles, None)

    assert err is None
    assert res == [None, test_player, test_map, test_b_tiles, test_s_tiles, None]