from flask import Blueprint, jsonify, make_response
from server.models import Restaurant, RestaurantPizza, db

# Create a Blueprint for restaurant routes
restaurant_bp = Blueprint('restaurant_bp', __name__, url_prefix='/restaurants')

@restaurant_bp.route('/', methods=['GET'])
def get_restaurants():
    """
    GET /restaurants
    Returns a list of all restaurants.
    """
    restaurants = Restaurant.query.all()
    # Serialize each restaurant object to a dictionary
    return jsonify([restaurant.to_dict() for restaurant in restaurants]), 200

@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    """
    GET /restaurants/<int:id>
    Returns details of a single restaurant and its pizzas.
    If not found, returns a 404 error.
    """
    # Fetch the restaurant by ID, including its associated restaurant_pizzas and pizzas
    restaurant = Restaurant.query.get(id)

    if not restaurant:
        # If restaurant not found, return a 404 error
        return jsonify({"error": "Restaurant not found"}), 404

    # Serialize the restaurant, including its pizzas
    # The to_dict method in Restaurant model handles pizza serialization
    return jsonify(restaurant.to_dict(include_pizzas=True)), 200

@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    """
    DELETE /restaurants/<int:id>
    Deletes a restaurant and all related RestaurantPizzas due to cascading delete.
    Returns 204 No Content on success.
    Returns 404 if the restaurant is not found.
    """
    restaurant = Restaurant.query.get(id)

    if not restaurant:
        # If restaurant not found, return a 404 error
        return jsonify({"error": "Restaurant not found"}), 404

    try:
        db.session.delete(restaurant)
        db.session.commit()
        # Return 204 No Content on successful deletion
        return make_response('', 204)
    except Exception as e:
        db.session.rollback()
        # Handle potential database errors during deletion
        return jsonify({"error": f"An error occurred while deleting the restaurant: {str(e)}"}), 500

