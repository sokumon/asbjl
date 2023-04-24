from flask import Flask, render_template, redirect, request, session
from absjl import app
from absjl.modals.dbschema import db, Subject ,Upload ,Student
import json

@app.get('/getallsubjectsupload')
def Subjects():    
    return render_template('Subjects.html')


    
@app.post('/allsubjectsupload')
def allsubjectsupload_post():
    if not 'email_id' in session:
        res_obj = {}
        res_obj.update({"status": 1})
        res_obj.update({"error": 'not logged in'})
        return json.dumps(res_obj)
    else:
        email_id = session['email_id']

        subject_id = '1'
    
        print(subject_id[0])
        print(email_id)
        # current_user = db.session.query(Student).filter_by(email_id = email_id).all()
        # print(current_user[0].id)
        subjectsupload = db.session.query(Upload).filter_by(subject_id = subject_id).all()
        

        
        subjectsupload_list = []
        for i in range(0,len(subjectsupload)):
            tmp_dict = {}
            # tmp_dict.update({"id":i[1].id})
            # tmp_dict.update({"name":mynotes[i].name})
            # tmp_dict.update({"year_name":subjectsupload[i].name})
            tmp_dict.update({"year_no":subjectsupload[i].filename})
            tmp_dict.update({"id":subjectsupload[i].subject_id})
            subjectsupload_list.append(tmp_dict)
        return json.dumps(subjectsupload_list)
