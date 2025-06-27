from server.config import db
from sqlalchemy.orm import validates

class Pizza(db.Model):
    """
    Pizza Model: Represents a pizza with a name and ingredients.
    Has a many-to-many relationship with Restaurant through RestaurantPizza.
    """
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)

    # Define the relationship to RestaurantPizza
    # 'restaurant_pizzas' is the backref name in RestaurantPizza
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        """
        Converts the Pizza object to a dictionary.
        """
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients
        }

    def __repr__(self):
        """
        String representation of the Pizza object.
        """
        return f'<Pizza {self.id}: {self.name}>'

