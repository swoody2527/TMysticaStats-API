import duckdb, pandas, pathlib, ast

ROOT_DIR = pathlib.Path(__file__).resolve().parents[2]
game_path = ROOT_DIR / "data" / "game_data.csv"
player_path = ROOT_DIR / "data" / "player_data.csv"

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
    



print(fetch_faction_winrate('dwarves', '2018', '2019', '4'))