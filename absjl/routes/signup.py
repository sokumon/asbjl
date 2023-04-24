from flask import Flask, render_template, redirect, request, session
from absjl.modals.dbschema import db, Student
from absjl import app
import json
import bcrypt
import bleach
import re

@app.get('/signup')
def signup():    
    return render_template('login.html')


@app.post('/signup')
def signup_post():
    data = request.get_json()
    email_id= bleach.linkify(bleach.clean(data['email_id']))
    password = data['password']
    firstname = bleach.linkify(bleach.clean(data['firstname']))
    lastname = bleach.linkify(bleach.clean(data['lastname']))
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(pat,email_id) and email_id.endswith("@apsit.edu.in"):
        email  = Student.query.filter_by(email_id=email_id).first()
        if email is None:
            bytePwd = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(bytePwd,salt)
            tmp_student = Student(email_id=email_id,password=hashed,firstname=firstname,lastname=lastname)
            db.session.add(tmp_student)
            db.session.commit()
            res_obj = {}
            res_obj.update({"status":"OK"})
            res_obj.update({"message":"Successful !. Please go ahead and login"})
            return json.dumps(res_obj)
        else:
            res_obj = {}
            res_obj.update({"status":"ERROR"})
            res_obj.update({"error":"Email already registered with"})
            return json.dumps(res_obj)
    else:
        res_obj = {}
        res_obj.update({"status":"ERROR"})
        res_obj.update({"error":"Check for valid Email-ID and use Organization/College provided Email-ID"})
        return json.dumps(res_obj)