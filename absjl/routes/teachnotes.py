from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/teachnotes')
def teachnotes():    
    return render_template('teachnotes.html')