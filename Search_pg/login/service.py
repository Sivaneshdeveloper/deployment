from routes import User
from routes import Client
from flask import redirect,flash
from Search_pg.main.application import app
from flask import request, render_template
from flask_login import LoginManager, login_user
digits = "0123456789"
app.config['SECRET_KEY'] = 'thisisasecretkey'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'validate.login'


@login_manager.user_loader
def load_user(user_id):
    return Client.query.get(int(user_id))


def loger():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        a = (User.query.filter_by(email=email)).first()
        b = Client.query.filter_by(email=email).first()

        if a!=None:
            if a.email == email and a.password == password:
                return redirect("/user_dashboard")

        elif b!=None:
            if b.email == email and b.password == password:
                login_user(b, remember=True)
                return redirect("/client_dashboard")
        else:
            flash("Invalid username and password!","danger")
            return redirect("/login")
    return render_template("login.html")


