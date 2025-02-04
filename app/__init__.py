from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes import main_route, cadastro
    app.register_blueprint(main_route.bp)
    app.register_blueprint(cadastro.bp)
    
    return app