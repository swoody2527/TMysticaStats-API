from pathlib import Path

root = Path(__file__).resolve().parent.parent

data = root / 'data'

GAME_DATA_PATH = data / 'game_data.csv'
PLAYER_DATA_PATH = data / 'player_data.csv'