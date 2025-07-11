from flask import Blueprint, jsonify, request
from ..models import factions_models


factions_bp = Blueprint('factions', __name__)



def validate_faction_inputs(faction, s_year, e_year, num_players):

    if not all([faction, s_year, e_year, num_players]):
        return 'Missing 1 or more parameters for search.', None
    
    try:
        s_year = int(s_year)
        e_year = int(e_year)
        num_players = int(num_players)
    except ValueError:
        return '1 or more invalid parameter type(s).', None
    
    if num_players > 6 or s_year < 2013 or e_year > 2025:
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
def get_faction_pick_rates():
    
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



