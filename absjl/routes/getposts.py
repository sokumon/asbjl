from flask import Flask, render_template, redirect, request, session
from absjl.modals.dbschema import db, Student ,Subject ,Posts
from absjl import app
import json



@app.post('/getposts')
def getposts():
    posts = db.session.query(Posts).all()
    
    posts_list = []
    for i in range(0,len(posts)):
        tmp_dict = {}
        # tmp_dict.update({"id":i[1].id})
        tmp_dict.update({"subject_posts":posts[i].subject})
        tmp_dict.update({"content_posts":posts[i].content})
        # tmp_dict.update({"created-time":posts[i].created})
        tmp_dict.update({"student_id":posts[i].Student_id})
        tmp_dict.update({"thread_id":posts[i].Thread_id})
        posts_list.append(tmp_dict)
    return json.dumps(posts_list)