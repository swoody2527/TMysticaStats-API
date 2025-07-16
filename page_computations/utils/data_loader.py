import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def load_game_and_player_data():
    
    env = os.getenv('APP_ENV', 'prod')

    if env == 'test':
        game_url = os.getenv('GAME_TEST_DATA_URL')
        player_url = os.getenv('PLAYER_TEST_DATA_URL')
    else:
        game_url = os.getenv('GAME_DATA_URL')
        player_url = os.getenv('PLAYER_DATA_URL')

    if not game_url or not player_url:
        raise ValueError("Missing one or more Google Drive data URLs in environment variables.")

    game_data = pd.read_csv(game_url)
    player_data = pd.read_csv(player_url)

    return game_data, player_data
