# tests/test_trends_endpoints.py

test_s_year = 2013
test_e_year = 2014


def test_win_rate_over_time(client):
    response = client.get(
        f"/api/trends/win-rate-ot?s_year={test_s_year}&e_year={test_e_year}"
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)

    year = next(iter(result.keys()))
    year_data = result[year]
    assert isinstance(int(year), int)
    assert isinstance(year_data, dict)

    faction = next(iter(year_data.keys()))
    win_rate = year_data[faction]
    assert isinstance(faction, str)
    assert isinstance(win_rate, (float, type(None)))


def test_pick_rate_over_time(client):
    response = client.get(
        f"/api/trends/pick-rate-ot?s_year={test_s_year}&e_year={test_e_year}"
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)

    year = next(iter(result.keys()))
    year_data = result[year]
    assert isinstance(int(year), int)
    assert isinstance(year_data, dict)

    faction = next(iter(year_data.keys()))
    pick_rate = year_data[faction]
    assert isinstance(faction, str)
    assert isinstance(pick_rate, float)


def test_map_picks_over_time(client):
    response = client.get(
        f"/api/trends/map-picks-ot?s_year={test_s_year}&e_year={test_e_year}"
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)

    year = next(iter(result.keys()))
    maps_for_year = result[year]
    assert isinstance(int(year), int)
    assert isinstance(maps_for_year, dict)

    map_code = next(iter(maps_for_year.keys()))
    games_played = maps_for_year[map_code]
    assert isinstance(map_code, str)
    assert isinstance(games_played, int)


def test_played_games_over_time(client):
    response = client.get(
        f"/api/trends/played-games-ot?s_year={test_s_year}&e_year={test_e_year}"
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)

    year = next(iter(result.keys()))
    games_count = result[year]
    assert isinstance(int(year), int)
    assert isinstance(games_count, int)
