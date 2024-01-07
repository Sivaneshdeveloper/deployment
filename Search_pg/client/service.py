from routes import Client,User
from routes import db
from flask import request,render_template, redirect,session,flash
from datetime import datetime
import smtplib
import math
import random
from Search_pg.main.application import app
app.secret_key="supersecuredsecretkey"
digits = "0123456789"


def getemail():
    if request.method == 'POST':
        email = request.form['email']
        a=User.query.filter_by(email=email).first()
        b= Client.query.filter_by(email=email).first()
        if a != None:
            flash("This email id has already registered in Buyer account!", "warning")
            redirect("/client_email")
        elif b==None:
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
            session['otp'] =OTP
            flash("Please check your email!","info")
            return redirect("/email_verification")
        elif b.email == email:
            flash("Email id has been already registered!", "warning")
            redirect("/client_email")
    return render_template("email.html")


def client_register():
    now = datetime.now()
    if "email" in session:
        user=session['email']

        if request.method == 'POST':
            date_time = now.strftime("%d/%m/%Y")
            # getting input with name = fname in HTML form
            first_name = request.form.get("firstname")

            # getting input with name = lname in HTML form
            last_name = request.form.get("lastname")
            password = request.form['password']
            object = Client(firstname=first_name, lastname=last_name, email=user, password=password,
                            created_by=date_time)
            db.session.add(object)
            db.session.commit()
            flash("Successfully account created!","success")
            return redirect("/login")
    else:
        flash("Session out, Please try again!", "info")
        return redirect("/client_email")

    return render_template("create.html")


def email_verification():
    if "otp" in session:
        OTP = session['otp']
        if request.method == 'POST':
            a = request.form['otp']
            if a == OTP:
                return redirect("/client_register")
            elif a!= OTP:
                flash("Please entered correct OTP!","danger")
                return redirect("/email_verification")
    else:
        flash("Session out, Please try again!", "info")
        return redirect("/client_email")

    return render_template("ren.html")

