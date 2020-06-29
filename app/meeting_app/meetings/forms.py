from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime
from meeting_app.models import Room, User


def check_date(FlaskForm,field):
  try:
    datetime.strptime(field.data, '%b %d, %Y')
  except:
    raise ValidationError("Invalid date value")

def check_end_date(FlaskForm,field):
  if(field.data):
    try:
      datetime.strptime(field.data, '%b %d, %Y')
    except:
      raise ValidationError("Invalid date value")


def check_time(FlaskForm,field):
  try:
    datetime.strptime(field.data, '%H:%M')
  except:
    raise ValidationError("Invalid time value")



class ReservingForm(FlaskForm):
  meeting_title = StringField("Meeting Title", validators=[DataRequired()])
  cr_room = Room.query.all()
  # room = SelectField("Meeting Room", choices=[("","Choose meeting room")]+[((room.created_room),(room.created_room)) for room in cr_room ], validators=[DataRequired()], coerce=str)
  room =SelectField("Meeting Room", validators=[DataRequired()], coerce=str)
  # my_choices = [("","Choose Employees")]+[((user.email),(user.email)) for user in User.query.filter_by(usertype="user")]
  # my_choices = [("","Choose Employees")]+[((user.email),(user.email)) for user in User.query.all()]
  # employee = SelectMultipleField("Employee",choices=my_choices, validators=[DataRequired()])
  employee = SelectMultipleField("Employee", validators=[DataRequired()])
  start_date = StringField("start", validators=[DataRequired(), check_date])
  end_date = StringField("end",validators=[check_end_date])
  start_time = StringField("start-date", validators=[DataRequired(),check_time])
  end_time = StringField("end-date", validators=[DataRequired(), check_time])
  submit = SubmitField("Create")



class  AddRoomForm(FlaskForm):
  add_room = StringField("Add Meeting Room", validators=[DataRequired()])
  submit = SubmitField("Create")