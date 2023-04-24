from flask import Flask,render_template,redirect,request,session
from absjl import app


@app.get('/logout')
def logout():
    if 'email_id' in session:
       session.pop('email_id', None)
    return redirect('/')

@app.post('/logout')
def poslogout():
    if 'email_id' in session:
       session.pop('email_id', None)
    return redirect('/')