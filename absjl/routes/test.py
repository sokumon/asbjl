from flask import Flask, render_template, redirect, request, session
from absjl import app
from absjl.modals.dbschema import Student, db, Upload
from werkzeug.utils import secure_filename
import os
from absjl import ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.get('/test')
def test_get():
    return render_template("test.html")

@app.post('/test')
def test():
    if request.method == 'POST':
        file = request.files['file']
        # info = request.get_json()
        # subject_name = info['name']
        # sem_no = info['sem_no']
        temp_name = secure_filename(file.filename.replace(" ", ""))
        file.save(secure_filename(file.filename.replace(" ", "")))
        filename = "absjl\\static\\uploads\\"+secure_filename(file.filename.replace(" ",""))
        cmd = "echo f | xcopy /f /y "+ temp_name+" "+filename
        print(cmd)
        os.system(cmd)

        if allowed_file(file.filename) == True:
            # return 'file uploaded successfully'
            email_id = session["email_id"]
            print(email_id)
            current_user = db.session.query(Student).filter_by(email_id = email_id).all()
            upload = Upload(filename=file.filename.replace(" ",""),Student_id = str(current_user[0].id), subject_id = session["subject_id"])
            # sem = Upload(sem_no = sem_no )                                  
            db.session.add(upload)
            db.session.commit()
            return f"Hello, {file.filename}"
        else:
            return f"FILE NOT IN PDF FORMAT, {file.filename}"
        
    




