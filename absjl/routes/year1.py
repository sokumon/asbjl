from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/year1')
def year1():    
    return render_template('Year-1.html')