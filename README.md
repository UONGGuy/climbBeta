# ClimbBeta

ClimbBeta is a web application that provides information about climbing gyms in London.
Users can browse gyms, view details, and submit ratings and reviews.The project is built using Flask, with a SQLite database and to be hosted on InfinityFree.

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
    # Navigate to the directory you want the repository to live in and on your terminal, input the below command:
    git clone https://github.com/UONGGuy/climbBeta.git
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
    # EITHER
    python run.py
    # OR
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
├── app                                     # Management of core website assets and functionality
│   ├── __init__.py                         # Initialises the Flask app and sets configurations
│   ├── models                              # Defines SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── association_tables.py
│   │   ├── base_model.py
│   │   ├── climbing_gym_features.py
│   │   ├── climbing_gyms.py
│   │   └── enums.py
│   ├── routes.py                           # Manages paths between URLs and functions handling calls when a page is visited
│   └── templates                           # Templates for the types of webpages to be generated
│       ├── base.html
│       ├── climbing_gym.html
│       └── index.html
│
├── config                                  # Contain different website environment configurations
│   ├── __init__.py
│   ├── development.py
│   ├── production.py
│   └── testing.py
│
├── database                                # Scripts allowing the website database to be managed (currently manual)
│   ├── __init__.py
│   ├── drop_tables.py
│   └── seed.py
│
├── tests                                   # Contains unit tests for website functionality
│   ├── __init__.py
│   ├── base_test.py
│   ├── conftest.py
│   ├── test_models.py
│   └── test_routes.py
│
├── check_tables.py                         # Display existing database tables in terminal
├── environment.yml                         # Package requirements file for Anaconda
├── requirements.txt                        # Package requirements file for pip
├── README.md                               # README file
└── run.py                                  # Script to run website

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
