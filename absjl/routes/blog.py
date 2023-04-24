from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/blog')
def blog():    
    return render_template('blog.html')