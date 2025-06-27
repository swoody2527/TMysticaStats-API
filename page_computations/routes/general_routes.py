from flask import Blueprint, jsonify
from ..models import general_models

general_bp = Blueprint('general', __name__)

@general_bp.route('/general/strongest-faction')
def get_strongest_faction():
    response = general_models.fetch_test_model()

    return jsonify(response)

