from flask import Blueprint, jsonify, request
from ..models import trends_models
from ..utils import validate_inputs as val


trends_bp = Blueprint('trends', __name__)


@trends_bp.route('/win-rate-ot')
def get_win_rates_over_time():

    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = val.validate_route_inputs(s_year, e_year)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        s_year, e_year, map, num_players, faction = inputs
        response = trends_models.fetch_winrates_over_time(s_year, e_year)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    


@trends_bp.route('/pick-rate-ot')
def get_pick_rates_over_time():

    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = val.validate_route_inputs(s_year, e_year)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        s_year, e_year, map, num_players, faction = inputs
        response = trends_models.fetch_pickrates_over_time(s_year, e_year)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@trends_bp.route('/map-picks-ot')
def get_map_pop_over_time():

    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = val.validate_route_inputs(s_year, e_year)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        s_year, e_year, map, num_players, faction = inputs
        response = trends_models.fetch_map_popularity_ot(s_year, e_year)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500



@trends_bp.route('/played-games-ot')
def get_played_games_ot():

    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = val.validate_route_inputs(s_year, e_year)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        s_year, e_year, map, num_players, faction = inputs
        response = trends_models.fetch_played_games_ot(s_year, e_year)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500