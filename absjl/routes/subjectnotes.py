from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/subjectnotes')
def subjectnotes():    
    return render_template('subjectnotes.html')