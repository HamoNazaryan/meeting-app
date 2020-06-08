from flask import render_template, request, Blueprint, url_for, redirect
from meeting_app.models import Meeting, User
from flask_login import current_user
from datetime import datetime, timedelta

main = Blueprint('main', __name__)


@main.route('/', methods=["GET", "POST"])
@main.route("/home", methods=["GET", "POST"])
def index():
  if current_user.is_authenticated:
    page=request.args.get('page',1,type=int)
    current_date = datetime(datetime.today().year, datetime.today().month, datetime.today().day)
    month = current_date - timedelta(days = 1)
    meetings = Meeting.query.filter(Meeting.end_date > month).order_by(Meeting.created_date.desc()).paginate(page=page,per_page=5)
    image_file = url_for('static', filename='/img/' + current_user.image_file)
    return render_template("index.html", isIndex=True,image_file=image_file,meetings=meetings,legend="All reserved meetings")
  else:
    return redirect(url_for('users.login'))
  # return render_template("index.html", meetingData = meetingData, isIndex=True)




