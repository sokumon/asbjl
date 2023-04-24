from flask import Flask, render_template, redirect, request, session
from absjl.modals.dbschema import db, Student
from absjl import app
import json


@app.post('/get_registered_students')
def get_registered_students():
    students = Student.query.order_by(Student.id).all()
    student_list = []
    for i in students:
        tmp_dict = {}
        tmp_dict.update({"id":i.id})
        tmp_dict.update({"email_id":i.email_id})
        tmp_dict.update({"firstname":i.firstname})
        tmp_dict.update({"lastname":i.lastname})
        student_list.append(tmp_dict)        
    return json.dumps(student_list)
        

