from flask import Flask, render_template, redirect, request, session
from absjl import app
from absjl.modals.dbschema import Posts, db, Subject , Student
import json
import bcrypt
import bleach
import random
from datetime import datetime

@app.post('/posts')
def recvpost():
    print(session)
    if not 'email_id' in session:
        res_obj = {}
        res_obj.update({"status": 1})
        res_obj.update({"error": 'not logged in'})
        return json.dumps(res_obj)
    else:
        data = request.get_json()
        new_content = data['content']
        thread_id = data['thread_id']
        print(thread_id)
        new_content = bleach.linkify(bleach.clean(new_content))
        current_time = datetime.now()
        firstname = data['firstname']
        current_user = db.session.query(Student).filter_by(firstname= firstname).all()
        print(current_user[0].id)
        # temp_file_name = 'temp_posts/'+ str(session['uid'])
        # cmd = f'echo {new_content} > {temp_file_name}.txt'
        # r = os.popen(cmd)
        # comd = f'/usr/bin/curl -X POST -F file=@{temp_file_name}.txt ' + '"http://127.0.0.1:5001/api/v0/add"'
        # result = os.popen(comd)
        # a = json.loads(result.read())
        # new_content_hash = a['Hash']
        # https://www.freecodecamp.org/news/javascript-dom-manipulation/#:~:text=In%20website%20development%2C%20DOM%20stands,very%20common%20in%20web%20development.
        post = Posts(subject=random.randrange(0,230802),content=new_content,created=current_time, Student_id= str(current_user[0].id),Thread_id = thread_id)
        db.session.add(post)
        db.session.commit()
        res_obj = {}
        res_obj.update({"status": 0})
        res_obj.update({"info": 'new post created successfully'})
        return json.dumps(res_obj)

         