from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/getnotes')
def getnotes():    
    return render_template('Mynotes.html')