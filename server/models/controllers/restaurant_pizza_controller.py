from flask import Blueprint, request, jsonify
from server.models import RestaurantPizza, Pizza, Restaurant, db

# Create a Blueprint for restaurant_pizza routes
restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    """
    POST /restaurant_pizzas
    Creates a new RestaurantPizza entry.
    Validates the price (1-30).
    Returns the new RestaurantPizza with associated pizza and restaurant details on success.
    Returns 400 Bad Request on validation error or if pizza/restaurant not found.
    """
    data = request.get_json()

    # Extract data from the request body
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Basic validation for presence of required fields
    if not all([price, pizza_id, restaurant_id is not None]):
        return jsonify({"errors": ["Missing required fields: price, pizza_id, restaurant_id"]}), 400

    # Check if pizza_id and restaurant_id exist
    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza:
        return jsonify({"errors": [f"Pizza with id {pizza_id} not found"]}), 404
    if not restaurant:
        return jsonify({"errors": [f"Restaurant with id {restaurant_id} not found"]}), 404

    try:
        # Create a new RestaurantPizza instance
        new_restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )

        # Add to session and commit to database
        db.session.add(new_restaurant_pizza)
        db.session.commit()

        # Prepare the success response with full details of pizza and restaurant
        # The .pizza and .restaurant relationships will be loaded by SQLAlchemy
        # We need to make sure the full details are included as per the requirement
        response_data = new_restaurant_pizza.to_dict(include_full_details=True)

        return jsonify(response_data), 201 # 201 Created

    except ValueError as e:
        db.session.rollback()
        # Handle validation errors from the model's @validates decorator
        return jsonify({"errors": [str(e)]}), 400
    except Exception as e:
        db.session.rollback()
        # Handle other potential database or server errors
        return jsonify({"errors": [f"An error occurred: {str(e)}"]}), 500

