from datetime import datetime
from flask import current_app
from sqlalchemy.orm import relationship
from meeting_app import db, login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  fname = db.Column(db.String(60), nullable=False)
  lname = db.Column(db.String(60), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='avatar.png')
  usertype = db.Column(db.String(20), nullable=False, default="user")
  password = db.Column(db.String(60), nullable=False)
  created_meetings = db.relationship('Meeting', backref='author', lazy=True)

  def get_reset_token(self, expires_sec=1800):
    s=Serializer(current_app.config['SECRET_KEY'], expires_sec)
    return s.dumps({'user_id' : self.id}).decode('utf-8')

  @staticmethod
  def verify_reset_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
      user_id = s.loads(token)['user_id']
    except:
      return None
    return User.query.get(user_id)

  def __repr__(self):
    return f"User('{self.fname}', '{self.lname}','{self.email}', '{self.usertype}', '{self.password}')"


class Meeting(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  room = db.Column(db.String(100), nullable=False)
  employee = db.Column(db.String(250), nullable=False)
  start_date = db.Column(db.Date, nullable=False)
  end_date = db.Column(db.Date)
  start_time = db.Column(db.Time, nullable=False)
  end_time = db.Column(db.Time, nullable=False)
  created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return f"Meeting('{self.room}', '{self.employee}', '{self.start_date}', '{self.end_date}','{self.start_time}', '{self.end_time}','{self.created_date}')"

