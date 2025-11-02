from flask import Flask
from flask_cors import CORS
from routes.video_routes import video_bp
from routes.quiz_routes import quiz_bp
from routes.user_routes import user_bp
import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app)

    # register blueprints
    app.register_blueprint(video_bp, url_prefix='/api/video')
    app.register_blueprint(quiz_bp, url_prefix='/api/quiz')
    app.register_blueprint(user_bp, url_prefix='/api/user')

    @app.route('/health')
    def health():
        return {"status": "ok"}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
