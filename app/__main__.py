# app/__main__.py
from app import create_app
from database.seed import seed_database

app = create_app()

seed_database()  
        
if __name__ == '__main__':
    app.run(debug=True)

