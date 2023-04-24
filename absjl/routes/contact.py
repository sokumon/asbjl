from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/contact')
def login():    
    return render_template('contact.html')