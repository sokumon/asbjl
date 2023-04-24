import this
from flask import Flask, render_template, redirect, request, session
from absjl.modals.dbschema import db, Student ,Subject , Votes ,Upload
from absjl import app
import json
from datetime import datetime

@app.post("/updatevotes")
def updatevotes():
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

        
        # task for u shravs find the student_id from this email_id joh apan aaj subhe kiya woh idhar paste kar
        data = request.get_json()
        posts_id =  data['posts_id']
        thread_id = data['thread_id']
        cateogory = data['cateogory']
        flag = 0
        global test
        global prev_points 
        if cateogory == "up":
            prev_points_query = db.session.query(Votes).all()
            if not prev_points_query:
                test = Votes(up_count = 1,down_count = 0, Student_id = current_user[0].id,Thread_id =thread_id ,Posts_id = posts_id)
                db.session.add(test)
                db.session.commit()
            else:
                prev_points = prev_points_query[0].up_count

                points = prev_points + 1
                test = Votes(up_count = points,down_count = prev_points_query[0].down_count, Student_id = current_user[0].id,Thread_id =thread_id ,Posts_id = posts_id)
                db.session.add(test)
                db.session.commit()
        else :
            prev_points_query = db.session.query(Votes).all()
            print(prev_points_query)
            prev_points = prev_points_query[0].dowm_count
            if prev_points == 0:
                flag =1
            else:
                points = prev_points - 1
            test = Votes(up_count = prev_points_query.down_count,down_count = points, Student_id = current_user[0].id,Thread_id =thread_id ,Posts_id = posts_id)
        
        

  
# Getting Today's Datetime
        today = datetime.now()
        # find me how to add sometime in db
        
        
        
        # shravs search for db.datetime something dekh kya scene ho raha hai usme

    subjectsupload_list = []
    tmp_dict = {}
    if flag == 1:
        tmp_dict.update({"status":"failed"})
    else:
        tmp_dict.update({"status":"success"})
    subjectsupload_list.append(tmp_dict)
    return json.dumps(subjectsupload_list)
