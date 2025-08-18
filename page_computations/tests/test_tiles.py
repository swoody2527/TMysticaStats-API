# tests/test_tiles_endpoints.py

test_map_id = '126fe960806d587c78546b30f1a90853b1ada468'
test_s_year = 2013
test_e_year = 2014
test_players = 4
test_faction = "dwarves"


def test_score_tile_frequency(client):
    response = client.get(
        f"/api/tiles/score-tile-freq?map_id={test_map_id}&s_year={test_s_year}&e_year={test_e_year}&num_players={test_players}&faction={test_faction}"
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)


def test_bonus_tile_popularity(client):
    response = client.get(
        f"/api/tiles/bonus-tile-pop?map_id={test_map_id}&s_year={test_s_year}&e_year={test_e_year}&num_players={test_players}&faction={test_faction}"
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)


def test_favor_tiles_by_faction(client):
    response = client.get(
        f"/api/tiles/favor-tiles-by-faction?map_id={test_map_id}&s_year={test_s_year}&e_year={test_e_year}&num_players={test_players}&faction={test_faction}"
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)


def test_town_tiles_by_faction(client):
    response = client.get(
        f"/api/tiles/town-tiles-by-faction?map_id={test_map_id}&s_year={test_s_year}&e_year={test_e_year}&num_players={test_players}&faction={test_faction}"
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)


def test_vp_gained_by_score_tile(client):
    response = client.get(
        f"/api/tiles/vp-gained-by-score-tile?map_id={test_map_id}&s_year={test_s_year}&e_year={test_e_year}&num_players={test_players}&faction={test_faction}"
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)
