from flask import Blueprint, jsonify
from server.models import Pizza

# Create a Blueprint for pizza routes
pizza_bp = Blueprint('pizza_bp', __name__, url_prefix='/pizzas')

@pizza_bp.route('/', methods=['GET'])
def get_pizzas():
    """
    GET /pizzas
    Returns a list of all pizzas.
    """
    pizzas = Pizza.query.all()
    # Serialize each pizza object to a dictionary
    return jsonify([pizza.to_dict() for pizza in pizzas]), 200

