# tests/test_maps_endpoints.py

test_map_id = '126fe960806d587c78546b30f1a90853b1ada468'
test_s_year = 2013
test_e_year = 2014


def test_games_per_map(client):
    response = client.get(
        f'/api/maps/games-per-map?map_id={test_map_id}&s_year={test_s_year}&e_year={test_e_year}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)
    assert result['map_id'] == test_map_id
    assert isinstance(result['games_played'], int)


def test_avg_players_per_map(client):
    response = client.get(
        f'/api/maps/avg-players-per-map?map_id={test_map_id}&s_year={test_s_year}&e_year={test_e_year}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)

    map_code = next(iter(result.keys()))
    playercount_distribution = result[map_code]

    assert isinstance(playercount_distribution, dict)
    assert isinstance(playercount_distribution['total_games'], int)

    example_pc_key = next(k for k in playercount_distribution.keys() if k.endswith('p'))
    assert isinstance(playercount_distribution[example_pc_key], float)


def test_faction_pickrate_on_map(client):
    response = client.get(
        f'/api/maps/faction-pickrate?map_id={test_map_id}&s_year={test_s_year}&e_year={test_e_year}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)

    faction_name = next(iter(result.keys()))
    pickrate_percent = result[faction_name]

    assert isinstance(faction_name, str)
    assert isinstance(pickrate_percent, float)


def test_faction_winrate_on_map(client):
    response = client.get(
        f'/api/maps/faction-winrate?map_id={test_map_id}&s_year={test_s_year}&e_year={test_e_year}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)

    faction_name = next(iter(result.keys()))
    winrate_percent = result[faction_name]

    assert isinstance(faction_name, str)
    assert isinstance(winrate_percent, float)


def test_avg_vp_per_map(client):
    response = client.get(
        f'/api/maps/avg-vp-per-map?map_id={test_map_id}&s_year={test_s_year}&e_year={test_e_year}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)

    faction_name = next(iter(result.keys()))
    average_vp = result[faction_name]

    assert isinstance(faction_name, str)
    assert isinstance(average_vp, int)


def test_performance_variation(client):
    response = client.get(
        f'/api/maps/performance-variation?map_id={test_map_id}&s_year={test_s_year}&e_year={test_e_year}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)

    faction_name = next(iter(result.keys()))
    winrate_delta = result[faction_name]

    assert isinstance(faction_name, str)
    assert isinstance(winrate_delta, float)
