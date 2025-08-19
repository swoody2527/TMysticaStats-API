from flask import Blueprint, jsonify, request
from ..models import trends_models
from ..utils import validate_inputs as val


trends_bp = Blueprint('trends', __name__)

"""
All functions in this module share the same arguments:

Args:
    s_year (int): Start year (inclusive).
    e_year (int): End year (inclusive).
"""


@trends_bp.route('/win-rate-ot')
def get_win_rates_over_time():

    """
    Returns faction win rates by year.

    Returns:
        dict: {
            <year>: {
            *For each faction*
                <faction>: float,   # Win rate percentage (0/100)
            },
        }
    """

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
    """
    Returns faction pick rates by year.

    Returns:
        dict: {
        *For each year*
            <year>: {
            *For each faction*
                <faction>: float,   # Pick rate percentage (0/100)
            }, 
        }
    """

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

    """
    Returns map popularity by year.

    Returns:
        dict: {
        *For each year*
            <year>: {
            *For each map*
                <map_id>: int,   # Number of games played on this map that year
            },
        }
    """

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

    """
    Returns the number of games played each year.

    Returns:
        dict: {
            <year>: int,   # Total games played in that year
        }
    """

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