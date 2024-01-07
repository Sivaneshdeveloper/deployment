from flask import Blueprint,render_template
from Search_pg.login.forget import first,user_forget_otp,client_forget_otp,user_password,client_password
from Search_pg.login.service import loger

validate = Blueprint('validate', __name__)


@validate.route("/forget_otp",methods=['GET','POST'])
def entry():
    return first()


@validate.route("/user_forget_otp",methods=['GET','POST'])
def a():
    return user_forget_otp()


@validate.route("/client_forget_otp",methods=['GET','POST'])
def cl():
    return client_forget_otp()


@validate.route("/user_password",methods=['GET','POST'])
def us():
    return user_password()


@validate.route("/client_password",methods=['GET','POST'])
def data():
    return client_password()


@validate.route("/choosen",methods=['GET','POST'])
def choose():
    return render_template("choosen.html")


@validate.route("/login", methods=['GET','POST'])
def login():
    return loger()

