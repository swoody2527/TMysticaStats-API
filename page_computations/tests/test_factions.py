
test_faction = 'dwarves'
test_s_year = 2013
test_e_year = 2014
test_players = 4


def test_faction_wr(client):
    response = client.get(
        f'/api/factions/faction-wr?faction={test_faction}&s_year={test_s_year}&e_year={test_e_year}&num_players={test_players}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)
    assert result['faction'] == test_faction
    assert isinstance(result['winrate'], float)
    assert isinstance(result['total_games'], int)
    assert isinstance(result['total_wins'], int)


def test_faction_pickrate(client):
    response = client.get(
        f'/api/factions/faction-pickrate?faction={test_faction}&s_year={test_s_year}&e_year={test_e_year}&num_players={test_players}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)
    assert result['faction'] == test_faction
    assert isinstance(result['pickrate'], float)
    assert isinstance(result['total_games'], int)
    assert isinstance(result['picked_games'], int)


def test_faction_wr_versus(client):
    response = client.get(
        f'/api/factions/faction-wr-versus?faction={test_faction}&s_year={test_s_year}&e_year={test_e_year}&num_players={test_players}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)

    opponent_faction = next(iter(result.keys()))
    opponent_stats = result[opponent_faction]

    assert isinstance(opponent_stats, dict)
    assert isinstance(opponent_stats['win_rate'], float)
    assert isinstance(opponent_stats['games_together'], int)
    assert isinstance(opponent_stats['games_won'], int)


def test_faction_wr_by_map(client):
    response = client.get(
        f'/api/factions/faction-wr-maps?faction={test_faction}&s_year={test_s_year}&e_year={test_e_year}&num_players={test_players}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)

    map_code = next(iter(result.keys()))
    map_stats = result[map_code]

    assert isinstance(map_stats, dict)
    assert isinstance(map_stats['win_rate'], float)
    assert isinstance(map_stats['total_games'], int)
    assert isinstance(map_stats['total_wins'], int)


def test_faction_avg_vp(client):
    response = client.get(
        f'/api/factions/faction-avg-vp?faction={test_faction}&s_year={test_s_year}&e_year={test_e_year}&num_players={test_players}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)
    assert isinstance(result['avg_vp'], float)
    assert isinstance(result['max_vp'], float)
    assert isinstance(result['min_vp'], float)
    assert isinstance(result['vp_25_percentile'], float)
    assert isinstance(result['vp_75_percentile'], float)


def test_faction_avg_vp_per_round(client):
    response = client.get(
        f'/api/factions/faction-avg-vp-per-round?faction={test_faction}&s_year={test_s_year}&e_year={test_e_year}&num_players={test_players}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)

    round_key = next(iter(result.keys()))
    avg_vp_for_round = result[round_key]

    assert isinstance(round_key, (str, int))
    assert isinstance(avg_vp_for_round, (int, float))


def test_faction_games_played(client):
    response = client.get(
        f'/api/factions/faction-games-played?faction={test_faction}&s_year={test_s_year}&e_year={test_e_year}&num_players={test_players}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)
    assert result['faction'] == test_faction
    assert isinstance(result['games_played'], int)


def test_faction_popularity_over_time(client):
    response = client.get(
        f'/api/factions/faction-popularity-ot?faction={test_faction}&s_year={test_s_year}&e_year={test_e_year}&num_players={test_players}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)

    year = next(iter(result.keys()))
    year_stats = result[year]

    assert isinstance(year_stats, dict)
    assert isinstance(year_stats['pick_rate'], float)
    assert isinstance(year_stats['total_games'], int)
    assert isinstance(year_stats['total_picks'], int)


def test_wr_by_playercount(client):
    response = client.get(
        f'/api/factions/wr-by-playercount?faction={test_faction}&s_year={test_s_year}&e_year={test_e_year}'
    )
    result = response.get_json()

    assert response.status_code == 200
    assert isinstance(result, dict)

    player_count = next(iter(result.keys()))
    stats_for_count = result[player_count]

    assert isinstance(stats_for_count, dict)
    assert isinstance(stats_for_count['win_rate'], float)
    assert isinstance(stats_for_count['total_games'], int)
    assert isinstance(stats_for_count['total_wins'], int)
