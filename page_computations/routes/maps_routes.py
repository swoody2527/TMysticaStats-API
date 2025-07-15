from flask import Blueprint, jsonify, request
from ..models import maps_models
from ..utils import validate_inputs as val

maps_bp = Blueprint('maps', __name__)



@maps_bp.route('/games-per-map')
def get_games_count_per_map():
    
    map = request.args.get('map_id')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = val.validate_route_inputs(s_year, e_year, map, require_map=True)
    print(inputs)
    if error:
        return jsonify({'error': error}), 400


    try:
        s_year, e_year, map, num_players, faction = inputs
        response = maps_models.fetch_games_played_by_map(s_year, e_year, map)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    


@maps_bp.route('/avg-players-per-map')
def get_pcount_distribution():
    
    map = request.args.get('map_id')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = val.validate_route_inputs(s_year, e_year, map, require_map=True)
    if error:
        return jsonify({'error': error}), 400


    try:
        s_year, e_year, map, num_players, faction = inputs
        response = maps_models.fetch_avg_players_per_map(s_year, e_year, map)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@maps_bp.route('/faction-pickrate')
def faction_map_pickrate():
    
    map = request.args.get('map_id')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = val.validate_route_inputs(s_year, e_year, map, require_map=True)
    if error:
        return jsonify({'error': error}), 400


    try:
        s_year, e_year, map, num_players, faction = inputs
        response = maps_models.fetch_pr_on_map(s_year, e_year, map)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@maps_bp.route('/faction-winrate')
def get_faction_map_winrate():
    
    map = request.args.get('map_id')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = val.validate_route_inputs(s_year, e_year, map, require_map=True)
    if error:
        return jsonify({'error': error}), 400


    try:
        s_year, e_year, map, num_players, faction = inputs
        response = maps_models.fetch_winrates_on_map(s_year, e_year, map)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    
@maps_bp.route('/avg-vp-per-map')
def get_avg_vp_per_map():
    
    map = request.args.get('map_id')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = val.validate_route_inputs(s_year, e_year, map, require_map=True)
    if error:
        return jsonify({'error': error}), 400

    try:
        s_year, e_year, map, num_players, faction = inputs
        response = maps_models.fetch_avg_vp_per_map(s_year, e_year, map)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    
@maps_bp.route('/performance-variation')
def get_performance_variation():
    
    map = request.args.get('map_id')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = val.validate_route_inputs(s_year, e_year, map, require_map=True)
    if error:
        return jsonify({'error': error}), 400

    try:
        s_year, e_year, map, num_players, faction = inputs
        response = maps_models.fetch_avg_vp_per_map(s_year, e_year, map)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500

    