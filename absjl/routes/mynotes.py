from unicodedata import name
from flask import Flask, render_template, redirect, request, session 
from absjl import app
from absjl.modals.dbschema import Student,Upload ,db
import json

@app.get('/getmynotes')
def getmynotes():    
    return render_template('mynotes.html')

@app.post('/getmynotes')
def getmynotes_post():
    if not 'email_id' in session:
        res_obj = {}
        res_obj.update({"status": 1})
        res_obj.update({"error": 'not logged in'})
        return json.dumps(res_obj)
    else:
        email_id = session['email_id']
        print(email_id)
        current_user = db.session.query(Student).filter_by(email_id = email_id).all()
        print(current_user[0].id)
        mynotes = db.session.query(Upload).filter_by(Student_id = current_user[0].id).all()
        
        mynotes_list = []
        for i in range(0,len(mynotes)):
            tmp_dict = {}
            # tmp_dict.update({"id":i[1].id})
            # tmp_dict.update({"name":mynotes[i].name})
            tmp_dict.update({"FILENAME":mynotes[i].filename})
            tmp_dict.update({"id":mynotes[i].Student_id})
            mynotes_list.append(tmp_dict)
        return json.dumps(mynotes_list)
