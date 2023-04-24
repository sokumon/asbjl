from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/discuss')
def discus():    
    return render_template('discuss.html')