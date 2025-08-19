from flask import Blueprint, jsonify, request
from ..models import prediction_models
from ..utils import validate_pred_inputs as val

predictions_bp = Blueprint('prediction', __name__)

# Redundant model, partially functional and not selected for use in final implementation.
@predictions_bp.route('/vp_prediction')
def get_vp_diff_predictions():
    
    is_factions = request.args.get('factions_included', 'false').lower() == 'true'
    num_players = request.args.get('num_players')
    map = request.args.get('map_id')
    game_bonus_tiles = request.args.getlist('bonus_tiles')
    score_tiles = request.args.getlist('score_tiles')
    game_factions = request.args.getlist('game_factions') if is_factions else []

    try:
        response = prediction_models.fetch_vp_score_prediction(num_players, map, 
                                                           game_bonus_tiles, score_tiles, game_factions)
        return jsonify(response), 200
    
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500


@predictions_bp.route('/win_prediction')
def get_win_prediction():

    """
    Predicts win probabilities for all factions not already selected in a game draft,
    based on map, number of players, bonus/score tiles, and chosen factions.

    Args:
        num_players (int): Number of players in the game.
        map_id (str): Map identifier.
        b_tiles (list[str]): List of bonus tile identifiers.
        s_tiles (list[str]): List of scoring tile identifiers.
        g_factions (list[str]): List of factions already selected in the draft. OPTIONAL

    Returns:
        dict:
              {
              *For each other faction than user selected*
                  <faction>: {
                      "win_prob": float,   # Predicted win probability (0/1)
                      "risk_level": int    # Risk level classification:
                                           #   1 = Low risk (>= 50% win prob)
                                           #   2 = Medium risk (30–49% win prob)
                                           #   3 = High risk (< 30% win prob)
                  },

              }
    """
    
    
    is_factions = request.args.get('factions_included', 'false').lower() == 'true'
    num_players = request.args.get('num_players')
    map = request.args.get('map_id')
    game_bonus_tiles = request.args.getlist('bonus_tiles')
    score_tiles = request.args.getlist('score_tiles')
    game_factions = request.args.getlist('game_factions') if is_factions else []

    error, inputs = val.validate_model_inputs(is_factions, num_players, map, game_bonus_tiles, score_tiles, game_factions)
    if error:
        return jsonify({'error': error}), 400

    try:
        faction_toggle, num_players, map, game_bonus_tiles, score_tiles, game_factions = inputs
        
        response = prediction_models.fetch_classification_prediction(num_players, map, 
                                                           game_bonus_tiles, score_tiles, game_factions)
        return jsonify(response), 200
    
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 500
