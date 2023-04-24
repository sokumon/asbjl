from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/year3')
def year3():    
    return render_template('Year-3.html')