# data_loader.py
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

_game_data = None
_player_data = None

def load_game_and_player_data():
    global _game_data, _player_data

    if _game_data is not None and _player_data is not None:
        return _game_data, _player_data

    env = os.getenv('APP_ENV', 'prod')

    game_url = os.getenv('GAME_TEST_DATA_URL') if env == 'test' else os.getenv('GAME_DATA_URL')
    player_url = os.getenv('PLAYER_TEST_DATA_URL') if env == 'test' else os.getenv('PLAYER_DATA_URL')

    if not game_url or not player_url:
        raise ValueError("Missing one or more data URLs in environment variables.")

    print("Loading data from:", game_url, player_url)

    _game_data = pd.read_csv(game_url)
    _player_data = pd.read_csv(player_url)

    return _game_data, _player_data
