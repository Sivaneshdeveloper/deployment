import datetime
from datetime import datetime
import base64
from flask_login import current_user
from flask import request, render_template,flash,redirect
from routes import Hostel,db


def dashboard():
    owner = current_user.id
    a=Hostel.query.filter_by(client_id=owner).all()
    if a==[]:
        flash("No Posts yet!")
        return render_template("client_dashboard.html")
    else:
        flash("Your Properties")
        return render_template('client_dashboard.html',hostels=a)


def post_hostel():
    now = datetime.now()
    if request.method == 'POST':
        date_time = now.strftime("%d/%m/%Y")
        owner=current_user.id
        client_name=current_user.firstname+" "+current_user.lastname
        # getting input with name = fname in HTML form
        name = request.form['name']
        phone = request.form['phone']
        price = request.form['price']
        advanceprice = request.form['advanceprice']
        location = request.form['location']
        room = request.form['room']
        food = request.form['food']
        gender = request.form['gender']
        pincode = request.form['pincode']
        # getting input with name = lname in HTML form
        sharing = request.form.getlist('rooms')
        facilities=request.form.getlist('facilities')
        bike=request.form['bike']
        car=request.form['car']
        locationlink=request.form['link']
        photos=request.files['file']
        data = photos.read()
        data = base64.b64encode(data)
        data = data.decode("UTF-8")
        object = Hostel(client_id=owner,location=location,hostel_name=name,sharing=sharing,price=price,pre_advanced=advanceprice,
                        g_location=locationlink,mobile=phone,facilities=facilities,pg_type=gender,room_type=room,
                        food_type=food,photos=data,bike_parking=bike,car_parking=car,created_by=date_time,updated_by=date_time,client_name=client_name,pincode=pincode)
        db.session.add(object)
        db.session.commit()
        return redirect("/client_dashboard")
    return render_template("hostel.html")


