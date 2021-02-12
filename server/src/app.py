from flask import Flask, redirect, url_for, render_template, request, session
from common import logger
from routes import main_bp
from datastore import db_session, init_db, login_manager

app = Flask(__name__)
app.secret_key = "hello"

@app.teardown_appcontext
def shutdown_session(exc):
    logger.error(exc)
    db_session.remove()

if __name__ == "__main__":
  logger.info("Starting server! Debug: True")
  with app.app_context():
    app.register_blueprint(main_bp)
    login_manager.init_app(app)
    init_db()

  app.run(host="0.0.0.0", port=8081, debug=True)
