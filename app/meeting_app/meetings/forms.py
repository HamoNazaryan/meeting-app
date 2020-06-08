from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime

from meeting_app.models import User, Meeting



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
  # room = StringField("Meeting room")
  employee = StringField("Employee", validators=[DataRequired()])
  start_date = StringField("start", validators=[DataRequired(), check_date])
  end_date = StringField("end",validators=[check_end_date])
  start_time = StringField("start-date", validators=[DataRequired(),check_time])
  end_time = StringField("end-date", validators=[DataRequired(), check_time])
  room = SelectField("Meeting Room", 
                    choices=[ ("", "Choose Meeting Room"),("Room 1", "Room 1"),
                    ("Room 2", "Room 2"),("Room 3", "Room 3"),("Room 4", "Room 4")], 
                    validators=[DataRequired()],)
  # division = SelectField(
  #   "Division",
  #   choices=[("default", "Select something"), ("option1", "Option 1"), ("option2", "Option 2")],
  #   validators=[DataRequired(), check_sel],
  #   widget=CustomSelect(),
  #   default="default",
  #   ) 
  submit = SubmitField("Create")

  print(User.query.all())


