from server.config import db
from sqlalchemy.orm import validates

class RestaurantPizza(db.Model):
    """
    RestaurantPizza Model: Join table between Restaurant and Pizza.
    Represents a specific pizza offered by a specific restaurant at a certain price.
    """
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    # Foreign Keys
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    # Define relationships (backrefs are defined in Restaurant and Pizza models)
    # restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas') # Not needed if backref is used
    # pizza = db.relationship('Pizza', back_populates='restaurant_pizzas') # Not needed if backref is used

    # Validation for price: must be between 1 and 30
    @validates('price')
    def validate_price(self, key, price):
        if not (1 <= price <= 30):
            raise ValueError("Price must be between 1 and 30")
        return price

    def to_dict(self, include_full_details=False):
        """
        Converts the RestaurantPizza object to a dictionary.
        Optionally includes full details of the associated pizza and restaurant.
        """
        data = {
            'id': self.id,
            'price': self.price,
            'pizza_id': self.pizza_id,
            'restaurant_id': self.restaurant_id
        }
        if include_full_details:
            # Safely access related objects; check if they exist to prevent errors if relationship is not loaded
            data['pizza'] = self.pizza.to_dict() if self.pizza else None
            data['restaurant'] = self.restaurant.to_dict() if self.restaurant else None
        return data

    def __repr__(self):
        """
        String representation of the RestaurantPizza object.
        """
        return f'<RestaurantPizza {self.id}: Price={self.price}, Rest_ID={self.restaurant_id}, Pizza_ID={self.pizza_id}>'
