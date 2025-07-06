from flask import Blueprint, jsonify
from ..models import factions_models

factions_bp = Blueprint('factions', __name__)

@factions_bp.route('/factions/faction-wr')
def get_strongest_faction_by_name():
    response = factions_models.test_factions()
    return jsonify(response)

