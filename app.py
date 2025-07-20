from flask import Flask
from flask_cors import CORS

from page_computations.routes.faction_routes import factions_bp
from page_computations.routes.maps_routes import maps_bp
from page_computations.routes.tile_routes import tiles_bp
from page_computations.routes.trends_routes import trends_bp

from page_computations.utils import data_loader, data_store

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(factions_bp, url_prefix='/api/factions')
    app.register_blueprint(maps_bp, url_prefix='/api/maps')
    app.register_blueprint(tiles_bp, url_prefix='/api/tiles')
    app.register_blueprint(trends_bp, url_prefix='/api/trends')

    game_data, player_data = data_loader.load_game_and_player_data()
    data_store.game_data = game_data
    data_store.player_data = player_data

    return app
