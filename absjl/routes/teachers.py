from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/teachers')
def teachers():    
    return render_template('teachers.html')