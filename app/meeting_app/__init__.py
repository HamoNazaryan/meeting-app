from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from meeting_app.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view='users.login'
login_manager.login_massage_category = "info"
mail=Mail()



def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(Config)
  db.init_app(app)
  bcrypt.init_app(app)
  login_manager.init_app(app)
  mail.init_app(app)
  with app.app_context():
    from meeting_app.main.routes import main
    from meeting_app.users.routes  import users
    from meeting_app.meetings.routes import meetings
    from meeting_app.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(meetings)
    app.register_blueprint(errors)

  return app

