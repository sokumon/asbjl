from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/profile')
def profile():    
    return render_template('profile.html')