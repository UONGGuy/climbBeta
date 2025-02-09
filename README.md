# ClimbBeta

ClimbBeta is a web application that provides information about climbing gyms in London.
Users can browse gyms, view details, and submit ratings and reviews.The project is built using Flask, with a SQLite database and hosted on InfinityFree.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

### Main features
- Browse climbing gyms in London
- View detailed information about each gym including available facilities, training boards, nearest transport options, and recurring events

### Additional features (works planned)
- Page for beginners informing them of climbing gym safety
- Include database for links to all waivers for all relevant activities (current offering is adult bouldering form only)
- Submit ratings and reviews for gyms
- User authentication and authorization
- Admin panel for managing content

## Installation

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Setup
1. **Clone the repository**:
    ```bash
    mkdir climbBeta
    git clone https://github.com/UONGGuy/climbBeta.git
    cd climbBeta
    ```
    
2. **Create and install dependencies to a virtal environment**:
    ```bash
    # If using pip
    python -m venv venv
    source venve/bin/activate # On Windows: venv/Scripts/activate
    pip install -r requirements.txt

    # If using conda
    conda env create -f environment.yml
    conda activate climbBeta
    ```

3. **Set up the database** (must be run before website creation):
    ```bash
    python database/seed.py
    ```

4. **Run the application**:
    ```bash
    flask run
    ```
    Visit ``http://127.0.0.1.5000`` in your web browser to see your application in action.

## Usage

- Homepage: Browse a list of climbing gyms in London.

- Gym Details: Click on a gym to view detailed information.

- User Authentication: Register and log in to submit ratings and reviews. (Additional)

Admin Panel: Access the admin panel to manage content. (Additional)

## Project Structure

```bash
climbBeta/
│
├── app/                        
│   ├── __init__.py             # Initialises the Flask app and sets configurations
│   ├── __main__.py             # Main execution logic allowing python -m app
│   ├── models.py               # Defines SQLAlchemy models
│   ├── enums.py                # Contains enums for the app
│   ├── routes.py               # Defines Flask routes/endpoints
│   ├── templates/              # HTML templates for rendering web pages
│   │   ├── base.html           # Base HTML template for layout
│   │   ├── index.html          # Homepage template
│   │   ├── climbing_gym.html   # Climbing gym details template
│   ├── __main__.py             # Entry point to run the Flask app
│
├── config/                     
│   ├── __init__.py             # Initialises the config module
│   ├── config.py               # Default config settings
│   ├── test_config.py          # Testing config settings
│
├── database/                   
│   ├── __init__.py             # Initialises the database module
│   ├── seed.py                 # Seeds the database with data
│   ├── drop_tables.py          # Drops and recreates database tables
│
├── tests/                      
│   ├── __init__.py             # Initialises the tests module
│   ├── base_test.py            # Base test class with common setup/teardown
│   ├── test_models.py          # Tests for SQLAlchemy models
│   ├── test_routes.py          # Tests for Flask routes
│
├── requirements.txt            # Project dependencies
├── environment.yml             # Conda environment file with dependencies
└── README.md                   # Project description and setup instructions
```

## Contributing

Contributions are welcome!
Please fork this repository and submit a pull request for any changes you would like to make.
Please understand responses may be slow as I am still new to collaborating on GitHub projects.

### Running unit tests

It would be great if you could write an accompanying unit test for each new functionality added so we can ensure that code can be well maintained and errors spotted quickly!

To run the full suite of unit tests, call:

```bash
python -m unittest discover tests
```

## License

Currently unknown!
