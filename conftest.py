import pytest
from app import create_app
from page_computations.utils import data_loader, data_store

@pytest.fixture
def client():
    import os
    os.environ['APP_ENV'] = 'test'

    app = create_app()
    app.config['TESTING'] = True

    game_data, player_data = data_loader.load_game_and_player_data()
    data_store.game_data = game_data
    data_store.player_data = player_data

    with app.test_client() as client:
        yield client
