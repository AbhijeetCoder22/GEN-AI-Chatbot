from flask import Flask
from flask_cors import CORS
from config import JWT_SECRET_KEY
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

    jwt = JWTManager(app)

    # Register Blueprints
    from .routes import login,register,api
    #login route
    app.register_blueprint(login.login_bp)
    #register route
    app.register_blueprint(register.register_bp, url_prefix='/register')
    #api route
    app.register_blueprint(api.api_bp, url_prefix="/api")

    return app