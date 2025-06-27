# server/app.py

from server.config import app, db, migrate
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp
from server.models import Restaurant, Pizza, RestaurantPizza # Import models for migrate to discover them

# Register blueprints to include their routes in the application
app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

# Define a root route for basic testing
@app.route('/')
def home():
    """
    Root route for the API.
    """
    return "<h1>Welcome to the Pizza Restaurant API!</h1>"

if __name__ == '__main__':
    # Run the Flask app
    # In a production environment, you would typically use a WSGI server like Gunicorn
    app.run(port=5555, debug=True)
