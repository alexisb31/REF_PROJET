from flask import Flask

def create_app():
    app = Flask(__name__)

   
    from app.routes import jsonld_routes
    app.register_blueprint(jsonld_routes)

    return app
