from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/downvote')
def downvote():    
    return render_template('downvote.html')