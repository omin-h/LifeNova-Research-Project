from .user_routes import user_bp
from .data_routes import data_bp

def init_routes(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(data_bp)
