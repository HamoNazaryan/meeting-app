import re
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,  ValidationError, optional
from flask_login import current_user
from meeting_app.models import User



# from flask import Flask
# app = Flask(__name__)
# with app.app_context():
#   user = User.query.filter_by(usertype="admin").first()
#   print(user)


def check_email(FlaskForm, field): 
  regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
  if(not re.search(regex,field.data)):
    raise  ValidationError('Invalid email address')



def check_pass(FlaskForm,field): 
  flag = 0
  while True:   
    if not re.search("[a-z]", field.data): 
        flag = -1
        break
    elif not re.search("[A-Z]", field.data): 
        flag = -1
        break
    elif not re.search("[0-9]", field.data): 
        flag = -1
        break
    elif re.search("\s", field.data): 
        flag = -1
        break
    else: 
        flag = 0
        break
  
  if flag ==-1: 
    raise  ValidationError('Password must contain at least one upper case, lower case and numeric character')


class SignUpForm(FlaskForm):
  fname = StringField("First Name", validators=[DataRequired(), Length(min=2, max=60)])
  lname = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=60)])
  email = StringField("Email", validators=[DataRequired(),  check_email])
  password = PasswordField("Password", validators = [DataRequired(),Length(min=6, max=60),check_pass])
  confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password")])
  submit = SubmitField("Sign Up")

  # def validate_username(self, username):
  #   user = User.query.filter_by(username=username.data).first()
  #   if user:
  #     raise ValidationError("The username is taken. Please choose a different one.")

 
  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError("The username is taken. Please choose a different one.")
    



class LoginForm(FlaskForm):
  email = StringField("Email", validators=[DataRequired(), Email()])
  password = PasswordField("Password", validators = [DataRequired(),Length(min=6, max=60)])
  remember = BooleanField("Remember Me")
  submit = SubmitField("Login")


class UpdateAccountForm(FlaskForm):
  fname = StringField("First Name", validators=[DataRequired(), Length(min=2, max=60)])
  lname = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=60)])
  email = StringField("Email", validators=[DataRequired(), Email(), check_email])
  picture = FileField('Update profile picture', validators=[FileAllowed(['jpg','png','jpeg'])])
  password = PasswordField("New password",  validators = [check_pass, optional(), Length(min=6, max=60)])
  confirm_password = PasswordField("Confirm Password", validators = [EqualTo("password")])
  submit = SubmitField("Update")

  def validate_email(self, email):
    if email.data != current_user.email:
      user = User.query.filter_by(email=email.data).first()
      if user:
        raise ValidationError("The username is taken. Please choose a different one.")


class RequestResetForm(FlaskForm):
  email = StringField("Email", validators=[DataRequired(), Email()])
  submit = SubmitField('Send Password Reset email')

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is None:
      raise ValidationError("There is no account with that email. You must register first.")


class ResetPasswordForm(FlaskForm):
  password = PasswordField('Password', validators=[DataRequired(),check_pass])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password'),check_pass])
  submit = SubmitField('Reset Password')
