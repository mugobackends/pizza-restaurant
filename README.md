🍕 Pizza Restaurant API
This project implements a RESTful API for managing pizza restaurants, pizzas, and the association between them using Flask, Flask-SQLAlchemy, and Flask-Migrate. It follows an MVC (Model-View-Controller) pattern for better organization.

🚀 Features
Manage Restaurants (CRUD-like: Get all, Get by ID, Delete)

Manage Pizzas (Get all)

Associate Pizzas with Restaurants at a specific price

Price validation for RestaurantPizza (1-30)

Cascading deletes: Deleting a Restaurant also deletes its associated RestaurantPizzas.

📂 Project Structure
.
├── server/
│   ├── __init__.py           # Package initializer
│   ├── app.py                # Main Flask application setup and blueprint registration
│   ├── config.py             # Database configuration and Flask/SQLAlchemy/Migrate initialization
│   ├── models/               # SQLAlchemy Models (data layer)
│   │   ├── __init__.py
│   │   ├── pizza.py
│   │   ├── restaurant.py
│   │   └── restaurant_pizza.py
│   ├── controllers/          # Route handlers (logic layer)
│   │   ├── __init__.py
│   │   ├── pizza_controller.py
│   │   ├── restaurant_controller.py
│   │   └── restaurant_pizza_controller.py
│   └── seed.py               # Script to seed the database with initial data
└── README.md                 # Project documentation

🛠 Setup Instructions
Follow these steps to set up and run the API locally.

Step 1: Clone the Repository (if applicable)
If you're starting from scratch, you'd initialize a new Git repository. If you received this code, clone it:

git clone <your-repo-url>
cd pizza-api-challenge # Or whatever your repository is named

Step 2: Create a Virtual Environment and Install Packages
It's highly recommended to use pipenv for dependency management.

# Install pipenv if you don't have it
pip install pipenv

# Navigate to the root directory of your project (where README.md is)
# Install Flask, Flask-SQLAlchemy, and Flask-Migrate
pipenv install flask flask_sqlalchemy flask_migrate

# Activate the virtual environment shell
pipenv shell

Step 3: Initialize and Run Database Migrations
Set the FLASK_APP environment variable and run the migration commands.

# Set the Flask application entry point
export FLASK_APP=server/app.py

# Initialize the migration repository (only once)
flask db init

# Create an initial migration script
flask db migrate -m "Initial migration"

# Apply the migrations to create tables in the database
flask db upgrade

Step 4: Seed the Database
Populate your database with some initial data.

python server/seed.py

Step 5: Run the Flask Application
# Ensure you are still in the pipenv shell and FLASK_APP is set
flask run
# The API will typically run on http://127.0.0.1:5000/ or http://localhost:5000/
# In this setup, it's configured to run on port 5555: http://127.0.0.1:5555/

🎯 API Routes
Here's a summary of the available API endpoints.

HTTP Method

Endpoint

Description

GET

/restaurants

Get a list of all restaurants.

GET

/restaurants/<int:id>

Get details of a single restaurant, including its pizzas.

DELETE

/restaurants/<int:id>

Delete a restaurant and all its associated RestaurantPizzas.

GET

/pizzas

Get a list of all pizzas.

POST

/restaurant_pizzas

Create a new RestaurantPizza entry.

1. GET /restaurants
Description: Retrieves a list of all pizza restaurants.

Example Request:

GET http://127.0.0.1:5555/restaurants

Example Success Response (Status: 200 OK):

[
    {
        "address": "123 Main St",
        "id": 1,
        "name": "Pizza Palace"
    },
    {
        "address": "456 Oak Ave",
        "id": 2,
        "name": "Dominic's Pizza"
    }
    // ... more restaurants
]

2. GET /restaurants/<int:id>
Description: Retrieves details for a specific restaurant, including the pizzas it offers.

Path Parameters:

id (integer): The ID of the restaurant.

Example Request:

GET http://127.0.0.1:5555/restaurants/1

Example Success Response (Status: 200 OK):

{
    "address": "123 Main St",
    "id": 1,
    "name": "Pizza Palace",
    "pizzas": [
        {
            "id": 1,
            "ingredients": "Tomato sauce, Mozzarella, Basil",
            "name": "Margherita"
        },
        {
            "id": 2,
            "ingredients": "Tomato sauce, Mozzarella, Pepperoni",
            "name": "Pepperoni"
        }
    ]
}

Example Error Response (Status: 404 Not Found):

{
    "error": "Restaurant not found"
}

3. DELETE /restaurants/<int:id>
Description: Deletes a restaurant and all associated RestaurantPizza entries.

Path Parameters:

id (integer): The ID of the restaurant to delete.

Example Request:

DELETE http://127.0.0.1:5555/restaurants/1

Example Success Response (Status: 204 No Content):
(No content in the response body)

Example Error Response (Status: 404 Not Found):

{
    "error": "Restaurant not found"
}

4. GET /pizzas
Description: Retrieves a list of all available pizzas.

Example Request:

GET http://127.0.0.1:5555/pizzas

Example Success Response (Status: 200 OK):

[
    {
        "id": 1,
        "ingredients": "Tomato sauce, Mozzarella, Basil",
        "name": "Margherita"
    },
    {
        "id": 2,
        "ingredients": "Tomato sauce, Mozzarella, Pepperoni",
        "name": "Pepperoni"
    }
    // ... more pizzas
]

5. POST /restaurant_pizzas
Description: Creates a new RestaurantPizza entry, linking a pizza to a restaurant with a specific price.

Request Body:

{
    "price": 5,
    "pizza_id": 1,
    "restaurant_id": 3
}

Validation Rules:

price: Must be an integer between 1 and 30 (inclusive).

Example Success Request:

POST http://127.0.0.1:5555/restaurant_pizzas
Content-Type: application/json

{
    "price": 17,
    "pizza_id": 1,
    "restaurant_id": 2
}

Example Success Response (Status: 201 Created):

{
    "id": 10,
    "pizza": {
        "id": 1,
        "ingredients": "Tomato sauce, Mozzarella, Basil",
        "name": "Margherita"
    },
    "pizza_id": 1,
    "price": 17,
    "restaurant": {
        "address": "456 Oak Ave",
        "id": 2,
        "name": "Dominic's Pizza"
    },
    "restaurant_id": 2
}

Example Error Response (Status: 400 Bad Request - Price Validation):

{
    "errors": ["Price must be between 1 and 30"]
}

Example Error Response (Status: 404 Not Found - Missing Pizza/Restaurant):

{
    "errors": ["Pizza with id 99 not found"]
}

🧪 Testing with Postman
To test the API endpoints using Postman:

Download Postman: If you don't have it, download Postman from https://www.postman.com/downloads/.

Import Collection:

Open Postman.

Click on the Import button in the top left.

Select Upload Files and choose the challenge-1-pizzas.postman_collection.json file (this file is referenced in the prompt, but not provided by me. You would need to create it based on the routes above or generate one from an OpenAPI spec).

Alternatively, you can manually create requests in Postman based on the "API Routes" section above.

Run API: Ensure your Flask API is running (flask run).

Send Requests: Select each request in the imported collection and click Send to test the endpoints. Verify the responses match the expected outcomes described in the "API Routes" section.

This README.md provides all the necessary information for setting up, running, and testing the API.