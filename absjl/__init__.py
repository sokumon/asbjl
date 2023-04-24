from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dkljsakljdlksajlk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///absjl.db'
db = SQLAlchemy(app)     

ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER']=os.path.join(os.getcwd(), 'absjl/static/uploads').translate(str.maketrans({'\\': '/'}))

from absjl.routes import login
from absjl.routes import home
from absjl.routes import teachers
from absjl.routes import teachnotes
from absjl.routes import year1
from absjl.routes import year2
from absjl.routes import year3
from absjl.routes import year4
from absjl.routes import about
from absjl.routes import blog
from absjl.routes import signup
from absjl.routes import functionalities
from absjl.routes import profile
from absjl.routes import test
from absjl.routes import logout
from absjl.routes import discuss
from absjl.routes import thread
from absjl.routes import posts         
from absjl.routes import upvote  
from absjl.routes import downvote  
from absjl.routes import getuploads 
from absjl.routes import mynotes
from absjl.routes import getallsubjects
from absjl.routes import allsubjectsupload
from absjl.routes import updatevotes
from absjl.routes import getposts 
from absjl.routes import getnotes
from absjl.routes import reader
from absjl.routes import getuploads
from absjl.routes import subjectnotes
from absjl.routes import test1




