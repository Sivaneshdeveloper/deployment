from flask import Blueprint,render_template
from routes import Hostel

from Search_pg.user.service import user_email,dashboard,user_register,user_email_verification,hostel_list

user = Blueprint('user', __name__)


@user.route("/user_email", methods=['GET','POST'])
def user_get_email():
    return user_email()


@user.route("/user_dashboard", methods=['GET','POST'])
def user_home():
    return dashboard()


@user.route("/user_register", methods=['GET','POST'])
def new_user():
    return user_register()


@user.route("/user_email_verification", methods=["GET","POST"])
def verification():
    return user_email_verification()


@user.route("/hostel_lists", methods=["GET","POST"])
def lists():
    return hostel_list()


@user.route("/view_property/<id>", methods=['GET','POST'])
def single(id):
    b = Hostel.query.filter_by(id=id).first()
    return render_template("view_property.html",hostels=b)