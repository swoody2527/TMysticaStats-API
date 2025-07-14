from flask import Blueprint, jsonify, request
from ..models import maps_models

maps_bp = Blueprint('maps', __name__)

def validate_maps_inputs(map, s_year, e_year):

    if not all([map, s_year, e_year]):
        return 'Missing 1 or more parameters for search.', None

    valid_maps = [
        '126fe960806d587c78546b30f1a90853b1ada468',
        '95a66999127893f5925a5f591d54f8bcb9a670e6',
        'be8f6ebf549404d015547152d5f2a1906ae8dd90',
        'fdb13a13cd48b7a3c3525f27e4628ff6905aa5b1',
        '91645cdb135773c2a7a50e5ca9cb18af54c664c4',
        '2afadc63f4d81e850b7c16fb21a1dcd29658c392'

    ]

    if map not in valid_maps:
        return 'Invalid map id.', None
    
    
    try:
        s_year = int(s_year)
        e_year = int(e_year)
    except ValueError:
        return '1 or more invalid parameter type(s).', None

    if s_year < 2013 or e_year > 2025:
        return 'Parameter out of bounds.', None
    
    return None, [map, s_year, e_year]


@maps_bp.route('/games-per-map')
def get_games_count_per_map():
    
    map = request.args.get('map_id')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = validate_maps_inputs(map, s_year, e_year)
    if error:
        return jsonify({'error': error}), 400


    try:
        response = maps_models.fetch_games_played_by_map(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    


@maps_bp.route('/avg-players-per-map')
def get_pcount_distribution():
    
    map = request.args.get('map_id')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = validate_maps_inputs(map, s_year, e_year)
    if error:
        return jsonify({'error': error}), 400


    try:
        response = maps_models.fetch_avg_players_per_map(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@maps_bp.route('/faction-pickrate')
def faction_map_pickrate():
    
    map = request.args.get('map_id')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = validate_maps_inputs(map, s_year, e_year)
    if error:
        return jsonify({'error': error}), 400


    try:
        response = maps_models.fetch_pr_on_map(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@maps_bp.route('/faction-winrate')
def get_faction_map_winrate():
    
    map = request.args.get('map_id')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = validate_maps_inputs(map, s_year, e_year)
    if error:
        return jsonify({'error': error}), 400


    try:
        response = maps_models.fetch_winrates_on_map(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    
@maps_bp.route('/avg-vp-per-map')
def get_avg_vp_per_map():
    
    map = request.args.get('map_id')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = validate_maps_inputs(map, s_year, e_year)
    if error:
        return jsonify({'error': error}), 400

    try:
        response = maps_models.fetch_avg_vp_per_map(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    
@maps_bp.route('/performance-variation')
def get_performance_variation():
    
    map = request.args.get('map_id')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = validate_maps_inputs(map, s_year, e_year)
    if error:
        return jsonify({'error': error}), 400

    try:
        response = maps_models.fetch_avg_vp_per_map(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500

    