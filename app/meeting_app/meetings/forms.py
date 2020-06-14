from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime
from meeting_app.models import Room


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



cr_room = Room.query.all()
for room in cr_room:
  print(room.created_room) 


class ReservingForm(FlaskForm):
  cr_room = Room.query.all()
  room = SelectField("Meeting Room", choices=[ ((room.created_room),(room.created_room)) for room in cr_room ], default=("Choose Meeting Room", "Choose Meeting Room"), coerce=str)
  employee = StringField("Employee", validators=[DataRequired()])
  start_date = StringField("start", validators=[DataRequired(), check_date])
  end_date = StringField("end",validators=[check_end_date])
  start_time = StringField("start-date", validators=[DataRequired(),check_time])
  end_time = StringField("end-date", validators=[DataRequired(), check_time])
  # room = SelectField("Meeting Room", coerce=str)
  # room = SelectField("Meeting Room", 
  #                   choices=[ ("", "Choose Meeting Room"),("Room 1", "Room 1"),
  #                   ("Room 2", "Room 2"),("Room 3", "Room 3"),("Room 4", "Room 4")], 
  #                   validators=[DataRequired()],)
  
  
  
  # division = SelectField(
  #   "Division",
  #   choices=[("default", "Select something"), ("option1", "Option 1"), ("option2", "Option 2")],
  #   validators=[DataRequired(), check_sel],
  #   widget=CustomSelect(),
  #   default="default",
  #   ) 
  submit = SubmitField("Create")

  # def __init__(self, *args, **kwargs):
  #   super(ReservingForm, self).__init__(*args, **kwargs)
  #   self.room.choices = [(room.created_room, room.created_room) for room in Room.query.all()]