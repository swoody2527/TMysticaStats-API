from flask import Blueprint, jsonify, request
from ..models import maps_models
from ..utils import validate_inputs as val

maps_bp = Blueprint('maps', __name__)

"""
All functions in this module share the same arguments:

Args:
    s_year (int): Start year.
    e_year (int): End year.
    map (str): Map identifier to analyze. REQUIRED
"""

@maps_bp.route('/games-per-map')
def get_games_count_per_map():

    """
    Returns the total number of games played on a given map.

    Returns:
        dict: {
            "map_id": str,        # Map identifier
            "games_played": int   # Number of games played on this map
        }
    """
    
    map = request.args.get('map_id')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = val.validate_route_inputs(s_year, e_year, map, require_map=True)
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

    """
    Returns the average player count distribution per map.

    Returns:
        dict: {
        *For each map*
            <map_id>: {
                "total_games": int,   # Total games played on the map
                "2p": float,          # Percentage of 2-player games
                "3p": float,          # Percentage of 3-player games
                "4p": float,          # Percentage of 4-player games
            },
        }
    """


    
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
    """
    Returns all faction pick rates for games played on a given map.

    Returns:
        dict: {
        *For each faction*
            <faction>: float,   # Percentage pick rate (0/100)
        }
    """
    
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

    """
    Returns all faction win rates for games played on a given map.

    Returns:
        dict: {
        *For each faction*
            <faction>: float,   # Win percentage (0/100)
            ...
        }
    """
    
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

    """
    Returns the average VP scored by each faction on a given map.

    Returns:
        dict: {
        *For each faction*
            <faction>: int,   # Average VP scored
        }
    """
    
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

    """
    Returns the difference in win rate for each faction on a specific map 
    compared to their global win rate across all maps.

    Returns:
        dict: {
        *For all factions*
            <faction>: float,   # Difference in win rate (global - map-specific)
        }
    """
    
    map = request.args.get('map_id')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')

    error, inputs = val.validate_route_inputs(s_year, e_year, map, require_map=True)
    if error:
        return jsonify({'error': error}), 400

    try:
        s_year, e_year, map, num_players, faction = inputs
        response = maps_models.fetch_performance_variation(s_year, e_year, map)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500

    