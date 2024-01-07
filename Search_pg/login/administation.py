import json

from flask import Blueprint,request,jsonify
from Search_pg.main.application import app
import jwt
from routes import User,Client,Hostel
from functools import wraps
admin = Blueprint('admin', __name__)
app.config['SECRET_KEY']= "supersecret"

@admin.route("/administration",methods=['POST'])
def login():
    get=request.json
    email=get['email']
    password = get['password']
    if email == 'searchstayinn@gmail.com' and password == 'sivanesh007':
        token = jwt.encode({'user': email}, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({"token": token})
    return "username and password are incorrect"


def token_request(f):
    @wraps(f)
    def decoarted(*args,**kwargs):
        access=request.headers['Authorization']
        if access.split(" ")[0]=="Bearer":
            token = access.split(" ")[1]
            if not token:
                return jsonify({'message': "token is missing"}), 403
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            except:
                return jsonify({"message": "token is invalid"}), 403
        else:
            return "please check the bearer token"

        return f(*args,**kwargs)
    return decoarted

@admin.route("/userlist",methods=['GET'])
@token_request
def userlist():
    a=User.query.all()
    list=[]
    content={}
    for result in a:
        content={"id":result.id,"firstname":result.firstname,"lastname":result.lastname,
                 "email":result.email,"password":result.password,
                 "created_by":result.created_by}
        list.append(content)
        content={}
        return jsonify({"Totaluser":len(a),"userlist":list})


@admin.route("/clientlist",methods=['GET'])
@token_request
def clientlist():
    a=Client.query.all()
    list=[]
    content={}
    for result in a:
        content={"id":result.id,"firstname":result.firstname,"lastname":result.lastname,
                 "email":result.email,"password":result.password,
                 "created_by":result.created_by}
        list.append(content)
        content={}
        return jsonify({"Totalclient":len(a),"clientlist":list})

@admin.route("/hostel_list",methods=['GET'])
@token_request
def hostel_list():
    a=Hostel.query.all()
    list=[]
    content={}
    for result in a:
        content={"Hostel_id":result.id,"client_id":result.client_id,"client_name":result.client_name,
                 "hostel_name":result.hostel_name,"location":result.location,"pg_type":result.pg_type,
                 "created_by":result.created_by}
        list.append(content)
        content={}
        return jsonify({"Total_hostel":len(a),"hostel_list":list})
