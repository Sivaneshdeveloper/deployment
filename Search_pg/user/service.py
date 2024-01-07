from routes import db
from routes import Hostel,User , Client
from flask import request,render_template, redirect,session,flash
from datetime import datetime
import smtplib
import math
import random
from Search_pg.main.application import app
app.secret_key="supersecuredsecretkey"
digits = "0123456789"


def user_email():
    if request.method == 'POST':
        email = request.form['email']
        a = User.query.filter_by(email=email).first()
        b = Client.query.filter_by(email=email).first()
        if b!=None:
            flash("This email id has already registered in Seller account!", "warning")
            redirect("/user_email")
        elif a == None:
            session['email'] = email
            OTP = ""
            for i in range(6):
                OTP += digits[math.floor(random.random() * 10)]
            otp = "Please Use the six digit code on Email verification " + OTP
            SUBJECT = 'Email OTP verification'
            TEXT = otp
            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("searchstayinn@gmail.com", "ztzviroqhhxgnupj")
            s.sendmail('&&&&&&&&&&&', email, message)
            session['otp'] = OTP
            flash("Please check your email!", "info")
            return redirect("/user_email_verification")
        elif b.email == email:
            flash("Email id has been already registered!", "warning")
            redirect("/user_email")
    return render_template("email.html")


def user_register():
    now = datetime.now()
    if "email" in session:
        user=session['email']
        if request.method == 'POST':
            date_time = now.strftime("%d/%m/%Y")
            # getting input with name = fname in HTML form
            first_name = request.form["firstname"]
            # getting input with name = lname in HTML form
            last_name = request.form["lastname"]
            password = request.form['password']
            object = User(firstname=first_name, lastname=last_name, email=user, password=password, created_by=date_time)
            db.session.add(object)
            db.session.commit()
            flash("Successfully account created!", "success")
            return redirect("/login")
    else:
        flash("Session out, Please try again!", "info")
        return redirect("/user_email")

    return render_template("create.html")


def user_email_verification():
    if "otp" in session:
        OTP=session['otp']
        if request.method == 'POST':
            a = request.form['otp']
            if a == OTP:
                return redirect("/user_register")
            elif a!= OTP:
                flash("Please entered correct OTP!", "danger")
                return redirect("/user_email_verification")
    else:
        flash("Session out, Please try again!", "info")
        return redirect("/user_email")

    return render_template("ren.html")


def dashboard():
    return render_template('search.html')


def hostel_list():
    if request.method=='POST':
        location=request.form['location']
        gender=request.form['gender']
        a=Hostel.query.filter_by(location=location,pg_type=gender).all()
        if a==[]:
            flash("No properties here!")
            return render_template('hostel_lists.html')
        else:
            flash("All Properties")
            return render_template('hostel_lists.html',hostels=a)

