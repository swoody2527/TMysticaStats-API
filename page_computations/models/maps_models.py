import pandas, pathlib, ast, os

from ..utils import data_loader as dl



game_data, player_data = dl.load_game_and_player_data()



def fetch_games_played_by_map(s_year, e_year, map):
    filtered_data = game_data[(game_data['year'].between(s_year, e_year)) &
                              (game_data['map'] == map)]
    
    return {
        'map_id': map,
        'games_played': len(filtered_data)
    }



def fetch_avg_players_per_map(s_year, e_year, map):
    filtered_data = game_data[game_data['year'].between(s_year, e_year)]

    all_maps = filtered_data['map'].value_counts()
    all_valid_maps = all_maps[all_maps > 100].index.tolist()

    players_per_map = {}

    for map in all_valid_maps:
        games_on_map = filtered_data[filtered_data['map'] == map]
        distribution = games_on_map['num_players'].value_counts(normalize=True)

        players_per_map[map] = {
            'total_games': len(games_on_map),
            **{f'{count}p': round(value * 100, 2)
            for count, value in distribution.items()}
        }
        


    return players_per_map



def fetch_pr_on_map(s_year, e_year, map):
    filtered_data = game_data[(game_data['year'].between(s_year, e_year)) &
                                  (game_data['map'] == map)]
    
    all_factions = set()
    
    for row in filtered_data['all_factions']:
        factions = ast.literal_eval(row)
        all_factions.update(f for f in factions if 'nofaction' not in f)
    
    pick_rates = {}
    for faction in all_factions:
        total_games = len(filtered_data)
        faction_games = filtered_data[filtered_data['all_factions'].apply(
            lambda row: faction in row
        )]
        pick_rates[faction] = round((len(faction_games) / total_games) * 100, 2)
    
    return pick_rates


def fetch_winrates_on_map(s_year, e_year, map):
    filtered_data = game_data[(game_data['year'].between(s_year, e_year)) &
                                      (game_data['map'] == map)]
    
    all_factions = set()
    
    for row in filtered_data['all_factions']:
        factions = ast.literal_eval(row)
        all_factions.update(f for f in factions if 'nofaction' not in f)

    win_rates = {}

    for faction in all_factions:
        total_picked_games = filtered_data[filtered_data['all_factions'].apply(
            lambda row: faction in row
        )]
        total_wins = total_picked_games[total_picked_games['winning_faction'] == faction]
        
        win_rates[faction] = round((len(total_wins) / len(total_picked_games)) * 100, 2)
    
    return win_rates



def fetch_avg_vp_per_map(s_year, e_year, map):
    filtered_data = player_data[(player_data['year'].between(s_year, e_year)) &
                                          (player_data['map'] == map)]
    

    all_factions = filtered_data['faction'].unique()

    average_vps = {}

    for faction in all_factions:
        all_faction_games = filtered_data[filtered_data['faction'] == faction]
        avg_vp = all_faction_games['vp_scored'].mean()
    
        average_vps[faction] = int(round(avg_vp))

    return average_vps




def fetch_performance_variation(s_year, e_year, map):
    non_map_filtered_data = game_data[(game_data['year'].between(s_year, e_year))]
    
    map_winrates = fetch_winrates_on_map(map, s_year, e_year)
    
    rel_factions = list(map_winrates.keys())


    global_winrates = {}

    for faction in rel_factions:
        total_picked_games = non_map_filtered_data[non_map_filtered_data['all_factions'].apply(
            lambda row: faction in row
        )]

        total_won_games = total_picked_games[total_picked_games['winning_faction'] == faction]
        global_winrates[faction] = round((len(total_won_games) / len(total_picked_games)) * 100, 2)

    winrate_diff = {}

    for key, value in map_winrates.items():
        winrate_diff[key] = round(global_winrates[key] - value, 2)

    return winrate_diff


