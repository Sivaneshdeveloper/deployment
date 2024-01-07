from routes import User
from routes import Client,db
from flask import redirect,flash
from flask import request,render_template,session
import math
import random
import smtplib
digits = "0123456789"


def first():
    if request.method == 'POST':
        email = request.form['email']
        a=User.query.filter_by(email=email).first()
        b = Client.query.filter_by(email=email).first()
        if a!=None :
            session['email']=email
            OTP = ""
            for i in range(6):
                OTP += digits[math.floor(random.random() * 10)]
            otp = "Please Use the six digit code on Email verification purpose for changing new password  " + OTP
            SUBJECT = 'Password Change request'
            TEXT = otp
            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("searchstayinn@gmail.com", "ztzviroqhhxgnupj")
            s.sendmail('&&&&&&&&&&&', email, message)
            session['otp'] = OTP
            flash("Please check your email!", "info")
            return redirect("/user_forget_otp")
        elif b!=None :
            session['email'] = email
            OTP = ""
            for i in range(6):
                OTP += digits[math.floor(random.random() * 10)]
            otp = "Please Use the six digit code on Email verification purpose for changing new password  " + OTP
            SUBJECT = 'Password Change request'
            TEXT = otp
            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("searchstayinn@gmail.com", "ztzviroqhhxgnupj")
            s.sendmail('&&&&&&&&&&&', email, message)
            session['otp'] = OTP
            flash("Please check your email!", "info")
            return redirect("/client_forget_otp")
        else:
            flash("Invalid email id","warning")
            return redirect("/forget_otp")
    return render_template("email.html")


def user_forget_otp():
    if "otp" in session:
        OTP = session['otp']
        if request.method == 'POST':
            a = request.form['otp']
            if a == OTP:
                return redirect("/user_password")
            elif a != OTP:
                flash("Please entered correct OTP!","danger")
                return redirect("/client_forget_otp")
    else:
        flash("Session out, Please try again!", "info")
        return redirect("/forget_otp")

    return render_template("ren.html")


def client_forget_otp():
    if "otp" in session:
        OTP = session['otp']
        if request.method == 'POST':
            a = request.form['otp']
            if a == OTP:
                return redirect("/client_password")
            elif a != OTP:
                flash("Please entered correct OTP!","danger")
                return redirect("/client_forget_otp")
    else:
        flash("Session out, Please try again!", "info")
        return redirect("/forget_otp")
    return render_template("ren.html")


def user_password():
    if "email" in session:
        user = session['email']
        if request.method == 'POST':
            a = request.form['password']
            b = User.query.filter_by(email=user).first()
            b.password = a
            db.session.commit()
            flash("Password has been changed!","success")
            return redirect("/login")
    else:
        flash("Session out, Please try again!", "info")
        return redirect("/forget_otp")
    return render_template("check.html")


def client_password():
    if "email" in session:
        user = session['email']
        if request.method == 'POST':
            a = request.form['password']
            b = Client.query.filter_by(email=user).first()
            b.password = a
            db.session.commit()
            flash("Password has been changed!", "success")
            return redirect("/login")
    else:
        flash("Session out, Please try again!", "info")
        return redirect("/forget_otp")
    return render_template("check.html")
