import pandas, pathlib, ast, os
from ..utils import data_loader as dl



game_data, player_data = dl.load_game_and_player_data()


def fetch_faction_winrate(s_year, e_year, faction, num_players=None):
    filtered_data = game_data[
        (game_data['year'].between(int(s_year), int(e_year))) &
        (game_data['num_players'] == int(num_players) if num_players is not None else True) &
        (game_data['all_factions'].apply(lambda row: faction in row))
    ]

    all_games = len(filtered_data)

    all_wins = len(filtered_data[(filtered_data['winning_faction'] == faction)])

    return {
        'faction': faction,
        'winrate': round((all_wins / all_games) * 100, 2),
        'total_games': all_games,
        'total_wins': all_wins
    }


def fetch_faction_pickrate(faction, s_year, e_year, num_players=None):
    filtered_data = game_data[
        (game_data['year'].between(int(s_year), int(e_year))) &
        (game_data['num_players'] == int(num_players) if num_players is not None else True)
    ]

    all_games = len(filtered_data)

    picked_games = len(filtered_data[
        (filtered_data['all_factions'].apply(lambda row: faction in row))
    ])

    return {
        'faction': faction,
        'pickrate': round((picked_games / all_games) * 100, 2),
        'total_games': all_games,
        'picked_games': picked_games
    }

def fetch_faction_wr_vs_others(faction, s_year, e_year, num_players=None):
    '''
    for all factions Y
    games where faction X and Y were in play
    games where faction X won
    '''
    user_faction = faction
    filtered_data = game_data[
        (game_data['year'].between(int(s_year), int(e_year))) &
        (game_data['num_players'] == int(num_players) if num_players is not None else True)
    ]

    all_factions = filtered_data['winning_faction'].unique()

    win_rates_versus = {}

    for comp_faction in all_factions:
        versus_data = filtered_data[
            filtered_data['all_factions'].apply(
                lambda row: user_faction in row and comp_faction in row
            )
]
        
        
        game_total = len(versus_data)
        if game_total == 0 or comp_faction == user_faction:
            continue
        
        win_total = len(versus_data[(versus_data['winning_faction'] == user_faction)])

        win_rates_versus[comp_faction] = {
            'win_rate': round((win_total / game_total) * 100, 2),
            'games_together': game_total,
            'games_won': win_total
        }

    return win_rates_versus


def fetch_winrate_by_map(faction, s_year, e_year, num_players=None):
    filtered_data = game_data[(game_data['year'].between(int(s_year), int(e_year))) &
            (game_data['num_players'] == int(num_players) if num_players is not None else True)]
    

    wins_by_map = {}
    all_maps = filtered_data['map'].unique()

    for map_code in all_maps:

        map_data = filtered_data[filtered_data['map'] == map_code] 

        games_with_faction = map_data[map_data['all_factions'].apply(
            lambda row: faction in row
        )]

        total_wins_on_map = games_with_faction[(games_with_faction['winning_faction'] == faction)]

        total_games = len(games_with_faction)
        total_wins = len(total_wins_on_map)

        if total_games < 5:
            continue

        wins_by_map[map_code] = {
            'win_rate': round((total_wins / total_games) * 100, 2),
            'total_games': total_games,
            'total_wins': total_wins
        }

    return wins_by_map


def fetch_faction_vp(faction, s_year, e_year, num_players=None):
    filtered_data = player_data[
        (player_data['faction'] == faction) &
        (player_data['year'].between(s_year, e_year)) &
        (player_data['num_players'] == num_players if num_players is not None else True)]
    

    vps = {
        'avg_vp': float(round(filtered_data['vp_scored'].mean(), 2)),
        'max_vp': float(round(filtered_data['vp_scored'].max(), 2)),
        'min_vp': float(round(filtered_data['vp_scored'].min(), 2)),
        'vp_25_percentile': float(round(filtered_data['vp_scored'].quantile(0.25), 2)),
        'vp_75_percentile': float(round(filtered_data['vp_scored'].quantile(0.75), 2)),

    }

    return vps


def fetch_faction_vp_by_round(faction, s_year, e_year, num_players=None):
    filtered_data = player_data[
        (player_data['faction'] == faction) &
        (player_data['year'].between(s_year, e_year)) &
        (player_data['num_players'] == num_players if num_players is not None else True)
    ]

    all_vps_by_round = filtered_data['vp_by_round']
    vp_df = pandas.DataFrame(ast.literal_eval(row) for row in all_vps_by_round)


    vp_avgs = vp_df.mean().to_dict()
    vp_avgs_round = {key: round(val) for key, val in vp_avgs.items()}

    return vp_avgs_round



def fetch_faction_games_played(faction, s_year, e_year, num_players=None):
    filtered_data = player_data[(player_data['faction'] == faction) &
            (player_data['year'].between(s_year, e_year)) &
            (player_data['num_players'] == num_players if num_players is not None else True)]
    

    return {
        'faction': faction,
        'games_played': len(filtered_data)
    }


def fetch_faction_popularity_ot(faction, s_year, e_year, num_players=None):
    filtered_data = game_data[
                (game_data['year'].between(s_year, e_year)) &
                (game_data['num_players'] == num_players if num_players is not None else True)]
    
    pick_rates = {}

    for year in range(s_year, e_year+1):
        years_games = filtered_data[filtered_data['year'] == year]
        print(years_games)
        total_games = len(years_games)
        
        total_picks = len(years_games[years_games['all_factions'].apply(
            lambda row: faction in row
        )])

        pick_rates[year] = {
            'pick_rate': round((total_picks / total_games) * 100, 2),
            'total_games': total_games,
            'total_picks': total_picks
        }
        
    return pick_rates


def fetch_faction_wr_by_playercount(faction, s_year, e_year, num_players=None):
    filtered_data = game_data[(game_data['year'].between(int(s_year), int(e_year))) &
                              (game_data['all_factions'].apply(lambda row: faction in row))]
    
    all_player_counts = sorted(filtered_data['num_players'].unique().tolist())
    if 1 in all_player_counts:
        all_player_counts.remove(1)

    win_rates = {}
    for count in all_player_counts:
        total_games = filtered_data[filtered_data['num_players'] == count]
        total_wins = total_games[total_games['winning_faction'] == faction]

        win_rates[count] = {
            'win_rate': round((len(total_wins) / len(total_games)) * 100, 2),
            'total_games': len(total_games),
            'total_wins': len(total_wins)
        }

    return win_rates


print(fetch_faction_games_played('dwarves', 2017, 2022, 4))

