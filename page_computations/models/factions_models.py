import duckdb, pandas, pathlib, ast, os

ROOT_DIR = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / 'data'

ENV = os.getenv('APP_ENV', 'prod')
print(ENV)

game_path = DATA_DIR / f"game{'_test_data' if ENV == 'test' else '_data'}.csv"
player_path = DATA_DIR / f"player{'_test_data' if ENV == 'test' else '_data'}.csv"

game_data = pandas.read_csv(game_path)
player_data = pandas.read_csv(player_path)


def fetch_faction_winrate(faction: str, s_year: int, e_year: int, num_players: int):
    filtered_data = game_data[
        (game_data['year'].between(int(s_year), int(e_year))) &
        (game_data['num_players'] == int(num_players)) &
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


def fetch_faction_pickrate(faction: str, s_year: int, e_year: int, num_players: int):
    filtered_data = game_data[
        (game_data['year'].between(int(s_year), int(e_year))) &
        (game_data['num_players'] == int(num_players))
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

def fetch_faction_wr_vs_others(faction, s_year, e_year, num_players):
    '''
    for all factions Y
    games where faction X and Y were in play
    games where faction X won
    '''
    user_faction = faction
    filtered_data = game_data[
        (game_data['year'].between(int(s_year), int(e_year))) &
        (game_data['num_players'] == int(num_players))
    ]

    all_factions = filtered_data['winning_faction'].unique()
    print(all_factions)

    win_rates_versus = {}

    for comp_faction in all_factions:
        versus_data = filtered_data[
            filtered_data['all_factions'].apply(
                lambda row: user_faction in row and comp_faction in row
            )
]
        
        
        game_total = len(versus_data)
        if game_total == 0:
            continue
        win_total = len(versus_data[(versus_data['winning_faction'] == user_faction)])

        win_rates_versus[comp_faction] = {
            'win_rate': round((win_total / game_total) * 100, 2),
            'games_together': game_total,
            'games_won': win_total
        }

    return win_rates_versus

print(fetch_faction_wr_vs_others('dwarves', 2016, 2018, 3))
