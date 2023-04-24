from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/reader')
def raeder():    
    return render_template('build/index.html')