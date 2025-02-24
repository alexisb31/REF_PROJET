from flask import Flask
from app.routes import jsonld_routes

app = Flask(__name__)

app.register_blueprint(jsonld_routes)

if __name__ == "__main__":
    app.run(debug=True, port=5001)