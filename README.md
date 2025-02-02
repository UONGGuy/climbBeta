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

### Additional features
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

3. **Set up the database**:
    ```bash
    flask db init
    flas gb migrate -m "Initial migration"
    flas db upgrade
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
climbbeta/
│
├── app.py                   # Main application file
├── models.py                # Database models
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── index.html           # Homepage
│   ├── gym.html             # Climbing gym details page
│
├── static/                  # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│
├── tests/                   # Tests directory
│   ├── __init__.py          # Makes this a package
│   ├── test_app.py          # Tests for the main application
│   ├── test_models.py       # Tests for database models
│   ├── test_routes.py       # Tests for routes
│
├── requirements.txt         # List of dependencies
├── environment.yml          # Conda environment file
└── README.md                # Project documentation
```

## Contributing

Contributions are welcome!
Please fork this repository and submit a pull request for any changes you would like to make.
Please understand responses may be slow as I am still new to collaborating on GitHub projects.

## License

Currently unknown!
