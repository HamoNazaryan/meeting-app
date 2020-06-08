from flask import render_template, url_for, flash, redirect, request, Blueprint,abort
from flask_login import login_user, current_user, logout_user, login_required
from meeting_app import db, bcrypt
from meeting_app.models import User, Meeting
from meeting_app.users.forms import SignUpForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from meeting_app.users.utils import save_picture, send_reset_mail
from datetime import datetime, timedelta

users = Blueprint('users', __name__)


@users.route("/signup", methods=["GET", "POST"])
def signUp():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = SignUpForm()
  if form.validate_on_submit():
    hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(fname=form.fname.data, lname=form.lname.data, email=form.email.data, password = hashed_pass)
    db.session.add(user)
    db.session.commit()
    flash(f'Your account has been created! You are now able to log in', 'success')
    return redirect(url_for('users.login'))
  return render_template('signup.html', title='SignUp', form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('main.index'))
    else:
      flash("Login Unsuccessful, Please check email and password", 'danger')
  return render_template('login.html', title='SignIn', form=form)


@users.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('users.login'))


@users.route('/account', methods=["GET", "POST"])
@login_required
def account():
  form = UpdateAccountForm()
  if form.validate_on_submit():
    if form.picture.data:
      picture_file = save_picture(form.picture.data)
      current_user.image_file = picture_file
    current_user.fname=form.fname.data
    current_user.lname=form.lname.data
    current_user.email=form.email.data
    if form.password.data:
      hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      current_user.password = hashed_pass
    db.session.commit()
    flash('Your account has bee updated!', 'success')
    return redirect(url_for('users.account'))
  elif request.method == 'GET':
    form.fname.data = current_user.fname
    form.lname.data = current_user.lname
    form.email.data = current_user.email
    form.password.data = current_user.password
  image_file = url_for('static', filename='/img/' + current_user.image_file)
  return render_template('account.html', title="Account", isIndex=True, image_file=image_file, form=form)


@users.route('/user/<int:id>')
def user_reserves(id):
  page = request.args.get('page', type=int)
  user=User.query.filter_by(id=id).first_or_404()
  current_date = datetime(datetime.today().year, datetime.today().month, datetime.today().day)
  date_now = current_date - timedelta(days = 1)
  meetings = Meeting.query.filter_by(author=user)\
                    .filter(Meeting.end_date > date_now).order_by(Meeting.created_date.desc())\
                    .paginate(page=page,per_page=5)
  return render_template('user_reserves.html', meetings=meetings, user=user)


@users.route("/reset_password", methods=['GET','POST'])
def reset_request():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = RequestResetForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    send_reset_mail(user)
    flash('An email has been sent with instructions to reset your password', 'info')
    return redirect(url_for('users.login'))
  return render_template('reset_request.html', title='Reset Password',form=form)


@users.route("/reset_password/<token>", methods=['GET','POST'])
def reset_token(token):
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  user = User.verify_reset_token(token)
  if user is None:
    flash('That is an invalid or expired token', 'danger')
    return redirect(url_for('users.reset_request'))
  form = ResetPasswordForm()
  if form.validate_on_submit():
    hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user.password = hashed_pass
    db.session.commit()
    flash(f'Your password has been updated! You are now able to log in', 'success')
    return redirect(url_for('users.login'))
  return render_template('reset_token.html', title='Reset Password', form=form)



@users.route("/users", methods=["GET", "POST"])
@login_required
def reg_users():
  if current_user.usertype == "admin":
    page=request.args.get('page',1,type=int)
    users = User.query.filter_by(usertype="user").paginate(page=page,per_page=5)
    image_file = url_for('static', filename='/img/' + current_user.image_file)
    return render_template("users.html", isIndex=True,image_file=image_file,users=users,legend="All registered users")
  else:
    return redirect(url_for('users.login'))



@users.route('/user/<int:user_id>/delete',methods=["POST"])
@login_required
def delete_user(user_id):  
  user= User.query.get_or_404(user_id)
  if ((current_user.usertype == "admin")):
    meetings=Meeting.query.filter_by(user_id = user.id).all()
    Meeting.query.filter_by(user_id = user.id).delete()
    db.session.delete(user)
    db.session.commit()
  else:
    abort(403)
  flash("User has been deleted!", 'danger')
  return redirect(url_for('users.reg_users'))