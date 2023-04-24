import json
from flask import Flask, render_template, redirect, request, session
from absjl import app
from absjl.modals.dbschema import db, Upload
from werkzeug.utils import secure_filename
import os
from absjl import ALLOWED_EXTENSIONS

@app.get("/test1")
def test1():
    return render_template("test1.html")

@app.post("/test1")
def test1_post():
    data = request.get_json()
    session["subject_id"] = data ["subject_id"]
    session["sem_no"] = data ["sem_no"]
    return json.dumps("something")