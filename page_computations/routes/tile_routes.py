from flask import Blueprint, jsonify, request
from ..models import tile_models
from ..utils import validate_inputs as val

tiles_bp = Blueprint('tiles', __name__)



@tiles_bp.route('/score-tile-freq')
def get_score_tile_frequency():
    map = request.args.get('map_id')
    num_players = request.args.get('num_players')
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    
    error, inputs = val.validate_route_inputs(s_year, e_year, map, num_players, faction)
    if error:
        return jsonify({'error': error}), 400


    try:
        response = tile_models.fetch_common_score_tile_order(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@tiles_bp.route('/bonus-tile-pop')
def get_bonus_tile_popularity():
    map = request.args.get('map_id')
    num_players = request.args.get('num_players')
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    
    error, inputs = val.validate_route_inputs(s_year, e_year, map, num_players, faction)
    if error:
        return jsonify({'error': error}), 400


    try:
        response = tile_models.fetch_popular_bonus_tiles_by_round(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500



@tiles_bp.route('/favor-tiles-by-faction')
def get_favor_tile_frequency():
    map = request.args.get('map_id')
    num_players = request.args.get('num_players')
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    
    error, inputs = val.validate_route_inputs(s_year, e_year, map, num_players, faction)
    if error:
        return jsonify({'error': error}), 400


    try:
        response = tile_models.fetch_favor_tiles_by_faction(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@tiles_bp.route('/town-tiles-by-faction')
def get_town_tile_frequency():
    map = request.args.get('map_id')
    num_players = request.args.get('num_players')
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    
    error, inputs = val.validate_route_inputs(s_year, e_year, map, num_players, faction)
    if error:
        return jsonify({'error': error}), 400


    try:
        response = tile_models.fetch_town_tiles_by_faction(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@tiles_bp.route('/vp-gained-by-score-tile')
def get_vp_gain_from_score_tile():
    map = request.args.get('map_id')
    num_players = request.args.get('num_players')
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    
    error, inputs = val.validate_route_inputs(s_year, e_year, map, num_players, faction)
    if error:
        return jsonify({'error': error}), 400


    try:
        response = tile_models.fetch_vp_gained_by_scoring_tile(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500