from flask import Flask, render_template, redirect, request, session
from absjl.modals.dbschema import db, Student ,Subject ,Upload
from absjl import app
import json



@app.post('/getuploads')
def getuploads():
    data = request.get_json()
    subject_id = data["subject_id"]
    uploads = db.session.query(Upload).filter_by(subject_id = subject_id).all()
    
    upload_list = []
    for i in range(0,len(uploads)):
        tmp_dict = {}
        # tmp_dict.update({"id":i[1].id})
        tmp_dict.update({"uploads":uploads[i].filename})
        # tmp_dict.update({"content_posts":uploads[i].Stude})
        # tmp_dict.update({"created-time":posts[i].created})
        tmp_dict.update({"student_id":uploads[i].Student_id})
        tmp_dict.update({"subject_id":uploads[i].subject_id})
        upload_list.append(tmp_dict)
    return json.dumps(upload_list)