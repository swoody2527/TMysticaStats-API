from flask import Blueprint, jsonify, request
from ..models import factions_models


factions_bp = Blueprint('factions', __name__)



def validate_faction_inputs(faction, s_year, e_year, num_players=None):

    valid_factions = [
        "auren", "witches",
        "mermaids", "swarmlings",
        "halflings", "cultists",
        "engineers", "dwarves",
        "alchemists", "chaosmagicians",
        "fakirs", "nomads",
        "giants", "darklings",
        "icemaidens", "yetis",
        "acolytes", "dragonlords",
        "shapeshifters", "riverwalkers"
        ]

    if faction not in valid_factions:
        return 'Invalid faction choice.', None


    if not all([faction, s_year, e_year]):
        return 'Missing 1 or more parameters for search.', None
    
    try:
        s_year = int(s_year)
        e_year = int(e_year)
        num_players = int(num_players) if num_players is not None else None
    except ValueError:
        return '1 or more invalid parameter type(s).', None
    
    if num_players and num_players > 6:
        return 'Player number filter out of bounds.', None 
    
    if s_year < 2013 or e_year > 2025:
        return 'Parameter out of bounds.', None
    
    return None, [faction, s_year, e_year, num_players]

@factions_bp.route('/faction-wr')
def get_strongest_faction_by_name():


    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = validate_faction_inputs(faction, s_year, e_year, num_players)
    if error:
        return jsonify({'error': error}), 400
    
    
    try:
        response = factions_models.fetch_faction_winrate(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    
@factions_bp.route('/faction-pickrate')
def get_faction_pick_rates():
    
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = validate_faction_inputs(faction, s_year, e_year, num_players)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        response = factions_models.fetch_faction_pickrate(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@factions_bp.route('/faction-wr-versus')
def get_faction_wr_versus():
    
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = validate_faction_inputs(faction, s_year, e_year, num_players)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        response = factions_models.fetch_faction_wr_vs_others(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    
@factions_bp.route('/faction-wr-maps')
def get_faction_wr_by_map():
    
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = validate_faction_inputs(faction, s_year, e_year, num_players)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        response = factions_models.fetch_winrate_by_map(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500

@factions_bp.route('/faction-avg-vp')
def get_faction_avg_vp():
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = validate_faction_inputs(faction, s_year, e_year, num_players)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        response = factions_models.fetch_faction_vp(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@factions_bp.route('/faction-avg-vp-per-round')
def get_faction_vp_by_round():
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = validate_faction_inputs(faction, s_year, e_year, num_players)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        response = factions_models.fetch_faction_vp_by_round(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

@factions_bp.route('/faction-games-played')
def get_faction_vp_by_round():
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = validate_faction_inputs(faction, s_year, e_year, num_players)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        response = factions_models.fetch_faction_games_played(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
    

    
    

@factions_bp.route('/faction-popularity-ot')
def get_faction_vp_by_round():
    faction = request.args.get('faction')
    s_year = request.args.get('s_year')
    e_year = request.args.get('e_year')
    num_players = request.args.get('num_players')

    error, inputs = validate_faction_inputs(faction, s_year, e_year, num_players)
    if error:
        return jsonify({'error': error}), 400
    
    try:
        response = factions_models.fetch_faction_popularity_ot(*inputs)
        return jsonify(response), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
