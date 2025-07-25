


def test_scor_freq(client):
    
    response = client.get('/api/tiles/score-tile-freq?s_year=2013&e_year=2014')
    assert response.status_code == 200


def test_vp_gain_by_score_tile(client):
    response = client.get('/api/tiles/vp-gained-by-score-tile?s_year=2014&e_year=2015')
    print(response.get_json())
    assert response.status_code == 200
