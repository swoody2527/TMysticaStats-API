import pandas, pathlib, ast, os

from ..utils import data_loader as dl



game_data, player_data = dl.load_game_and_player_data()


def fetch_winrates_over_time(s_year, e_year):
    filtered_data = game_data[game_data['year'].between(s_year, e_year)]



    win_rates_overtime = {}

    for year in range(s_year, e_year + 1):
        year_data = filtered_data[filtered_data['year'] == year]
        
        unique_factions = set(faction
            for row in year_data['all_factions']
            for faction in ast.literal_eval(row) if 'nofaction' not in faction
        )
        
        win_rates_overtime[year] = {}
        for faction in unique_factions:
            total_faction_apps = year_data[year_data['all_factions'].apply(
                lambda row: faction in row
            )]

            total_faction_wins = total_faction_apps[total_faction_apps['winning_faction'] == faction]

            if len(total_faction_apps) > 0:
                win_rate = round((len(total_faction_wins) / len(total_faction_apps)) * 100, 2)
            else:
                win_rate = None

            win_rates_overtime[year][faction] = win_rate
    return win_rates_overtime


def fetch_pickrates_over_time(s_year, e_year):
    filtered_data = game_data[game_data['year'].between(s_year, e_year)]

    pickrates_over_time = {}
    for year in range(s_year, e_year+1):
        year_data = filtered_data[filtered_data['year'] == year]

        unique_factions = set(
            faction
            for row in year_data['all_factions']
            for faction in ast.literal_eval(row) if 'nofaction' not in faction
        )
        pickrates_over_time[year] = {}
        for faction in unique_factions:
            total_games = len(year_data)

            total_picks = year_data[year_data['all_factions'].apply(
                lambda row: faction in row
            )]

            pickrates_over_time[year][faction] = round((len(total_picks) / total_games) * 100, 2)



    return pickrates_over_time



def fetch_map_popularity_ot(s_year, e_year):
    filtered_data = game_data[game_data['year'].between(s_year, e_year)]

    map_games_over_time = {}
    for year in range(s_year, e_year + 1):
        year_data = filtered_data[filtered_data['year'] == year]

        map_counts = year_data['map'].value_counts()

        map_games_over_time[year] = map_counts.to_dict()

    return map_games_over_time


def fetch_played_games_ot(s_year, e_year):

    games_per_year = {}

    for year in range(s_year, e_year+1):
        year_data = game_data[game_data['year'] == year]
        games_per_year[year] = len(year_data)

    return games_per_year