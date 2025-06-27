from server.config import db
from sqlalchemy.orm import validates

class Restaurant(db.Model):
    """
    Restaurant Model: Represents a restaurant with a name and address.
    Has a many-to-many relationship with Pizza through RestaurantPizza.
    When a Restaurant is deleted, all associated RestaurantPizzas should be deleted (cascading delete).
    """
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)

    # Define the relationship to RestaurantPizza
    # 'restaurant_pizzas' is the backref name in RestaurantPizza
    # cascade="all, delete-orphan" ensures that when a restaurant is deleted,
    # all related RestaurantPizza entries are also deleted.
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy=True, cascade="all, delete-orphan")

    # Add a validation for restaurant name to be unique and not empty
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Restaurant name cannot be empty")
        # You could also add a check for uniqueness here if required:
        # existing_restaurant = Restaurant.query.filter_by(name=name).first()
        # if existing_restaurant and existing_restaurant.id != self.id:
        #     raise ValueError("Restaurant name must be unique")
        return name

    # Add a validation for address to not be empty
    @validates('address')
    def validate_address(self, key, address):
        if not address:
            raise ValueError("Restaurant address cannot be empty")
        return address


    def to_dict(self, include_pizzas=False):
        """
        Converts the Restaurant object to a dictionary.
        Optionally includes a list of pizzas served by the restaurant.
        """
        data = {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }
        if include_pizzas:
            # Get unique pizzas through restaurant_pizzas relationship
            # Note: We need to serialize the pizza objects, not the RestaurantPizza objects directly
            data['pizzas'] = [
                rp.pizza.to_dict() for rp in self.restaurant_pizzas
            ]
        return data

    def __repr__(self):
        """
        String representation of the Restaurant object.
        """
        return f'<Restaurant {self.id}: {self.name}>'

