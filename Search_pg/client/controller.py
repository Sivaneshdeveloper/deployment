from flask import Blueprint,render_template,redirect
from flask_login import login_required
from Search_pg.client.service import client_register, email_verification,getemail
from Search_pg.client.hostel_service import dashboard,post_hostel
from routes import Hostel,db

client = Blueprint('client', __name__)


@client.route("/client_email", methods=['GET','POST'])
def email():
    return getemail()


@client.route("/client_dashboard", methods=['GET','POST'])
@login_required
def client_home():
    return dashboard()


@client.route("/client_register", methods=['GET','POST'])
def new_user():
    return client_register()


@client.route("/email_verification", methods=["GET","POST"])
def verification():
    return email_verification()


@client.route("/publish_hostel", methods=['GET','POST'])
@login_required
def publish_hostel():
    return post_hostel()


@client.route("/view_property/<id>", methods=['GET','POST'])
def single(id):
    b = Hostel.query.filter_by(id=id)
    return render_template("view_property.html",hostels=b)


@client.route("/delete_property/<id>", methods=['GET','POST'])
@login_required
def remove(id):
    object = Hostel.query.filter_by(id=id).first()
    db.session.delete(object)
    db.session.commit()
    return redirect("/client_dashboard")

