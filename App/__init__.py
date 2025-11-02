from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes.home import home_bp
    from .routes.servizi import servizi_bp
    #from .routes.team import team_bp
    #from .routes.contatti import contatti_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(servizi_bp)
    #app.register_blueprint(team_bp)
    #app.register_blueprint(contatti_bp)

    return app
