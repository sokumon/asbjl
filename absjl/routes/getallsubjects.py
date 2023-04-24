from flask import Flask, render_template, redirect, request, session
from absjl.modals.dbschema import db, Student ,Subject
from absjl import app
import json


@app.post('/getallsubjects')
def getallsubjects():
    subjects = Subject.query.order_by(Subject.id).all()
    subjects_list = []
    for i in range(0,len(subjects)):
        tmp_dict = {}
        # tmp_dict.update({"id":i[1].id})
        tmp_dict.update({"name":subjects[i].name})
        tmp_dict.update({"name":subjects[i].name})
        tmp_dict.update({"year_no":subjects[i].year_no})
        tmp_dict.update({"sem_no":subjects[i].sem_no})
        subjects_list.append(tmp_dict)    
    return json.dumps(subjects_list)
    
        
        