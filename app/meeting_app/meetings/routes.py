from flask import render_template, Blueprint, url_for, flash, redirect, request, abort
from flask_login import current_user, login_required
from meeting_app import db
from meeting_app.models import Meeting
from meeting_app.meetings.forms import ReservingForm
from datetime import datetime, timedelta, date
from sqlalchemy import or_, and_



meetings = Blueprint('meetings', __name__)


# from flask import Flask, current_app, has_app_context
# print(current_app)

# from meeting_app.models import Room, User
# from meeting_app import create_app

# # from meeting_app import create_app
# # app=create_app()
# ff= create_app()

# with ff.app_context():
#   # user = User.query.all()
#   room = Room.query.all()
#   print(room)



@meetings.route("/archive", methods=['GET', "POST"])
@login_required
def archive():
  page=request.args.get('page',1,type=int)
  current_date = datetime(datetime.today().year, datetime.today().month, datetime.today().day)
  date_now = current_date - timedelta(days = 1)
  meetings = Meeting.query.filter(Meeting.end_date <= date_now).order_by(Meeting.created_date.desc()).paginate(page=page,per_page=5)

  image_file = url_for('static', filename='/img/' + current_user.image_file)
  return render_template("archive.html", isIndex=True,image_file=image_file,meetings=meetings,legend="Archive")




@meetings.route("/reserve/new", methods=["GET", "POST"])
@login_required
def reserve_new():
  form = ReservingForm()
  # form = ReservingForm(room = "Choose Meeting Room")
  image_file = url_for('static', filename='/img/' + current_user.image_file)
  if form.validate_on_submit():
    st_date=datetime.strptime(form.start_date.data, '%b %d, %Y').date()
    st_time=datetime.strptime(form.start_time.data, '%H:%M').time()
    end_time=datetime.strptime(form.end_time.data, '%H:%M').time()
    if (form.end_date.data):
      end_date=datetime.strptime(form.end_date.data, '%b %d, %Y').date()
    else:
      end_date = st_date
    reserve_check = Meeting.query.filter_by(room = form.room.data)\
                                  .filter(
                                    or_(
                                      and_(end_date >= Meeting.start_date, end_date <= Meeting.end_date),
                                      and_(end_date >= Meeting.end_date, st_date <= Meeting.end_date)
                                    ))\
                                    .filter(
                                      or_(
                                        and_(end_time >= Meeting.start_time, end_time <= Meeting.end_time),
                                        and_(end_time >= Meeting.end_time, st_time <= Meeting.end_time)
                                      )).all()

    if reserve_check:
      flash("Meeting room in this time already reserved for another meeting", 'danger')
      return redirect(url_for('meetings.reserve_new'))
    
    meetings=Meeting(room=form.room.data, employee=form.employee.data, 
                    start_date=st_date,
                    end_date=end_date,
                    start_time=st_time,
                    end_time=end_time,
                    author=current_user)
    db.session.add(meetings)
    db.session.commit()
    flash('Meeting reserved!', 'success')
    return redirect(url_for('main.index'))
  return render_template('create_reserve.html', title='Reserve Meeting', 
                        form=form, isIndex=True, image_file=image_file, legend="Reserve Meeting")


@meetings.route('/reserve/<int:meeting_id>/update',methods=['GET',"POST"])
@login_required
def update_reserve(meeting_id):
  current_date = datetime(datetime.today().year, datetime.today().month, datetime.today().day)
  date_now = (current_date - timedelta(days = 1)).date()
  meetings= Meeting.query.get_or_404(meeting_id) 
  if meetings.end_date <= date_now:
    abort(403)

  if meetings.author == current_user or current_user.usertype=="admin":
    form = ReservingForm()

    if form.validate_on_submit():
      
      st_date=datetime.strptime(form.start_date.data, '%b %d, %Y').date()
      st_time=datetime.strptime(form.start_time.data, '%H:%M').time()
      end_time=datetime.strptime(form.end_time.data, '%H:%M').time()
      if (form.end_date.data):
        end_date=datetime.strptime(form.end_date.data, '%b %d, %Y').date()
      else:
        end_date = st_date
      reserve_check = Meeting.query.filter_by(room = form.room.data)\
                                    .filter(
                                      or_(
                                        and_(end_date >= Meeting.start_date, end_date <= Meeting.end_date),
                                        and_(end_date >= Meeting.end_date, st_date <= Meeting.end_date)
                                      ))\
                                      .filter(
                                        or_(
                                          and_(end_time >= Meeting.start_time, end_time <= Meeting.end_time),
                                          and_(end_time >= Meeting.end_time, st_time <= Meeting.end_time)
                                        )).all()
      print(reserve_check)
      current_res = False
      for res in reserve_check:
        if res.id==meetings.id:
          current_res = True
      print("meetings.id =", meetings.id)
      if reserve_check and not current_res:
        flash("Meeting room in this time already reserved for another meeting", 'danger')
        return redirect(url_for('meetings.update_reserve', meeting_id=meetings.id))
      meetings.room = form.room.data
      meetings.employee = form.employee.data
      meetings.start_date =st_date
      meetings.start_time = st_time
      meetings.end_time = end_time
      meetings.created_date = datetime.utcnow()
      meetings.end_date=end_date
      db.session.commit()
      flash("Your meeting has been updated!", 'success')
      return redirect(url_for('main.index', meeting_id=meetings.id))
    elif request.method == "GET":
      form.room.data = meetings.room
      form.employee.data=meetings.employee
      form.start_date.data = meetings.start_date.strftime('%b %d, %Y')
      if (meetings.end_date):
        form.end_date.data = meetings.end_date.strftime('%b %d, %Y')
      form.start_time.data = meetings.start_time.strftime('%H:%M')
      form.end_time.data = meetings.end_time.strftime('%H:%M')
  else:
    abort(403)

  return render_template('create_reserve.html', title="Update Meeting", 
                        form = form, legend="Update  Meeting")


@meetings.route('/reserve/<int:meeting_id>/delete',methods=["POST"])
@login_required
def delete_reserve(meeting_id):  
  meeting= Meeting.query.get_or_404(meeting_id)
  if ((meeting.author == current_user) or (current_user.usertype == "admin")):
    db.session.delete(meeting)
    db.session.commit()
    pass
  else:
    abort(403)
  flash("Your meeting has been deleted!", 'danger')
  return redirect(request.referrer)

