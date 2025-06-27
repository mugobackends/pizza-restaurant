from server.app import app # Import the app instance to get the context
from server.config import db
from server.models import Restaurant, Pizza, RestaurantPizza

def seed_data():
    """
    Seeds the database with initial Restaurant, Pizza, and RestaurantPizza data.
    """
    with app.app_context():
        # Drop all tables and recreate them to ensure a clean slate
        db.drop_all()
        db.create_all()

        print("Database cleared and recreated.")

        # Create some restaurants
        restaurant1 = Restaurant(name="Pizza Palace", address="123 Main St")
        restaurant2 = Restaurant(name="Dominic's Pizza", address="456 Oak Ave")
        restaurant3 = Restaurant(name="Mama Mia's Pizzeria", address="789 Pine Ln")
        restaurant4 = Restaurant(name="Gourmet Slice", address="101 Elm Blvd")

        db.session.add_all([restaurant1, restaurant2, restaurant3, restaurant4])
        db.session.commit()
        print("Restaurants created.")

        # Create some pizzas
        pizza1 = Pizza(name="Margherita", ingredients="Tomato sauce, Mozzarella, Basil")
        pizza2 = Pizza(name="Pepperoni", ingredients="Tomato sauce, Mozzarella, Pepperoni")
        pizza3 = Pizza(name="Veggie Delight", ingredients="Tomato sauce, Mozzarella, Bell peppers, Onions, Mushrooms")
        pizza4 = Pizza(name="Meat Lovers", ingredients="Tomato sauce, Mozzarella, Sausage, Bacon, Ham")
        pizza5 = Pizza(name="Hawaiian", ingredients="Tomato sauce, Mozzarella, Ham, Pineapple")

        db.session.add_all([pizza1, pizza2, pizza3, pizza4, pizza5])
        db.session.commit()
        print("Pizzas created.")

        # Create some restaurant-pizza relationships with prices
        # Pizza Palace offers Margherita and Pepperoni
        rp1 = RestaurantPizza(restaurant=restaurant1, pizza=pizza1, price=12)
        rp2 = RestaurantPizza(restaurant=restaurant1, pizza=pizza2, price=15)

        # Dominic's Pizza offers Pepperoni and Veggie Delight
        rp3 = RestaurantPizza(restaurant=restaurant2, pizza=pizza2, price=14)
        rp4 = RestaurantPizza(restaurant=restaurant2, pizza=pizza3, price=13)

        # Mama Mia's Pizzeria offers Margherita, Meat Lovers, and Hawaiian
        rp5 = RestaurantPizza(restaurant=restaurant3, pizza=pizza1, price=11)
        rp6 = RestaurantPizza(restaurant=restaurant3, pizza=pizza4, price=18)
        rp7 = RestaurantPizza(restaurant=restaurant3, pizza=pizza5, price=16)

        # Gourmet Slice offers Margherita and Veggie Delight
        rp8 = RestaurantPizza(restaurant=restaurant4, pizza=pizza1, price=10)
        rp9 = RestaurantPizza(restaurant=restaurant4, pizza=pizza3, price=12)


        db.session.add_all([rp1, rp2, rp3, rp4, rp5, rp6, rp7, rp8, rp9])
        db.session.commit()
        print("RestaurantPizzas created.")

        print("Database seeding complete!")

if __name__ == '__main__':
    seed_data()
