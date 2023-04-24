from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/year4')
def year4():    
    return render_template('Year-4.html')