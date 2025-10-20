from flask import Flask
from flask_cors import CORS
from config import config
from app.database import db, migrate
from app.cache import cache

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    CORS(app)
    
    from app.routes import parts, compatibility, builds
    app.register_blueprint(parts.bp, url_prefix='/api/v1/parts')
    app.register_blueprint(compatibility.bp, url_prefix='/api/v1/compatibility')
    app.register_blueprint(builds.bp, url_prefix='/api/v1/builds')
    
    @app.route('/health')
    def health():
        return {'status': 'ok'}, 200
    
    return app