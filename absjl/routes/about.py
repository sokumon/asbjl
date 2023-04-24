from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/about')
def about():    
    return render_template('about.html')