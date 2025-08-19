from flask import Blueprint, jsonify, request
from ..models import factions_models
from ..utils import validate_inputs as val


factions_bp = Blueprint('factions', __name__)



@factions_bp.route('/faction-wr')
def get_strongest_faction_by_name():

    """
    Calculate winrate statistics for a given faction.

    Args:
        *Identical across all endpoints in factions.*
        
        faction (str): Faction name to evaluate (e.g., "dwarves"). REQUIRED
        s_year (int): Start year (inclusive).
        e_year (int): End year (inclusive).
        num_players (int, optional): Filter games by player count.

    Returns:
        dict: {
            "faction": str,         # Faction name
            "winrate": float,       # Percentage winrate (0/100)
            "total_games": int,     # Number of games played
            "total_wins": int       # Number of games won
        }
    """

    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = val.validate_route_inputs(s_year, e_year, faction=faction, num_players=num_players, require_faction=True)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        s_year, e_year, map, num_players, faction = inputs
        response = factions_models.fetch_faction_winrate(faction, s_year, e_year, num_players)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    
@factions_bp.route('/faction-pickrate')
def get_faction_pick_rates():

    """
    Calculate how often a faction is picked (Pickrate).

    Returns:
        dict: {
            "faction": str,         # Faction name
            "pickrate": float,      # Percentage pickrate (0/100)
            "total_games": int,     # Number of games played
            "picked_games": int     # Number of games won
        }
    """
    
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = val.validate_route_inputs(s_year, e_year, faction=faction, num_players=num_players, require_faction=True)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        s_year, e_year, map, num_players, faction = inputs
        response = factions_models.fetch_faction_pickrate(faction, s_year, e_year, num_players)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@factions_bp.route('/faction-wr-versus')
def get_faction_wr_versus():

    """
    Returns faction winrate for all scenerios where each other faction
    is being played. e.g winrate when dwarves are present

    Returns:
        dict: {
        *For each faction*              # Dict entry for all other 19 factions
            'faction': dict: {        
                'win_rate: float,       # Win rate of user selected faction against other faction
                'games_together: int,   # Total games both appeared
                'games_won': int        # Total games user selected faction won
            },         

        }
    """
    
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = val.validate_route_inputs(s_year, e_year, faction=faction, num_players=num_players, require_faction=True)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        s_year, e_year, map, num_players, faction = inputs
        response = factions_models.fetch_faction_wr_vs_others(faction, s_year, e_year, num_players)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    
@factions_bp.route('/faction-wr-maps')
def get_faction_wr_by_map():

    """
    Returns faction winrate for all maps
    is being played. e.g winrate when dwarves are played on Original map

    Returns:
        dict: {
        *For each map*              # Dict entry for all maps
            >map_id>: dict: {        
                'win_rate: float,       # Win rate of user selected faction on map
                'total_games: int,      # Total games on map
                'total_wins': int       # Total games user selected faction won on map
            },         

        }
    """
    
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = val.validate_route_inputs(s_year, e_year, faction=faction, num_players=num_players, require_faction=True)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        s_year, e_year, map, num_players, faction = inputs
        response = factions_models.fetch_winrate_by_map(faction, s_year, e_year, num_players)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500

@factions_bp.route('/faction-avg-vp')
def get_faction_avg_vp():
    
    """
    Returns faction Victory Point statistics.


    Returns:
        dict: {
            "avg_vp": float,            # Total average VP scored
            "max_vp": float,            # Highest VP scored
            "min_vp": float,            # Lowest VP scored
            "vp_25_percentile": float,  # Lower quartile
            'vp_75_percentile': float   # Upper quartile
        }
    """
    
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = val.validate_route_inputs(s_year, e_year, faction=faction, num_players=num_players, require_faction=True)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        s_year, e_year, map, num_players, faction = inputs
        response = factions_models.fetch_faction_vp(faction, s_year, e_year, num_players)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@factions_bp.route('/faction-avg-vp-per-round')
def get_faction_vp_by_round():

    """
    Returns the average VP scored by a faction across game rounds.

    Returns:
        dict: {
            *For each round*
            <round_index>: int,  # Average VP scored in that round
        }
    """
    
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = val.validate_route_inputs(s_year, e_year, faction=faction, num_players=num_players, require_faction=True)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        s_year, e_year, map, num_players, faction = inputs
        response = factions_models.fetch_faction_vp_by_round(faction, s_year, e_year, num_players)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@factions_bp.route('/faction-games-played')
def get_faction_games_played():

    """
    Returns the total number of games played by a faction.

    Returns:
        dict: {
            "faction": str,        # Faction name
            "games_played": int    # Number of games played
        }
    """

    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = val.validate_route_inputs(s_year, e_year, faction=faction, num_players=num_players, require_faction=True)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        s_year, e_year, map, num_players, faction = inputs
        response = factions_models.fetch_faction_games_played(faction, s_year, e_year, num_players)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

    
    

@factions_bp.route('/faction-popularity-ot')
def get_faction_pop_over_time():

    """
    Returns yearly pick rate statistics for a faction.

    Returns:
        dict: {
        *For each year*
            <year>: {
                "pick_rate": float,     # Pick percentage (0–100)
                "total_games": int,     # Total games played that year
                "total_picks": int      # Times faction was picked
            },
            ...
        }
    """
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = val.validate_route_inputs(s_year, e_year, faction=faction, num_players=num_players, require_faction=True)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        s_year, e_year, map, num_players, faction = inputs
        response = factions_models.fetch_faction_popularity_ot(faction, s_year, e_year, num_players)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@factions_bp.route('/wr-by-playercount')
def get_faction_vp_by_playercount():

    """
    Returns winrate statistics for a faction across different player counts.

    Returns:
        dict: {
        *For each player count*
            <player_count>: {
                "win_rate": float,      # Win percentage (0/100)
                "total_games": int,     # Number of games with that player count
                "total_wins": int       # Number of wins with that player count
            },
            ...
        }
    """

    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = val.validate_route_inputs(s_year, e_year, faction=faction, num_players=num_players, require_faction=True)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        s_year, e_year, map, num_players, faction = inputs
        response = factions_models.fetch_faction_wr_by_playercount(faction, s_year, e_year, num_players)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
