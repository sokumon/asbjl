from flask import Flask, render_template, redirect, request, session
from absjl import app
from absjl.modals.dbschema import db, Votes

@app.get('/upvote')
def upvote():    
    return render_template('upvote.html')