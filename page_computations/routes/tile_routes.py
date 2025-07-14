from flask import Blueprint, jsonify, request
from ..models import tile_models

tiles_bp = Blueprint('tiles', __name__)


@tiles_bp.route('/score-tile-freq')
def get_score_tile_frequency():
    scoring_tiles = request.args.getlist('s_tile')
    bonus_tiles = request.args.getlist('b_tiles')
    map = request.args.get('map_id')
    num_players = request.args.get('num_players')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    

