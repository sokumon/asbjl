from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/year2')
def year2():    
    return render_template('YEAR-2.html')