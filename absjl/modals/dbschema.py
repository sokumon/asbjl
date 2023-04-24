from absjl import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String(30),  nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False,unique=False)
    firstname = db.Column(db.String(15), nullable=False, unique=False)
    lastname = db.Column(db.String(15), nullable=False, unique=False)
    # email_id= db.Column(db.String(15), nullable=False, unique=True)
    # password = db.Column(db.String(300), nullable=False)
    # profile_pic = db.Column(db.String(300), nullable=False)


    
class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(30),  nullable=False, unique=True)
    created = db.Column(db.String(100), nullable=False,unique=False)
    Student_id = db.Column(db.Integer,  db.ForeignKey(Student.id))
    
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject= db.Column(db.String(30),  nullable=False, unique=True)
    content = db.Column(db.String(1000) , nullable =False , unique = False)
    created = db.Column(db.DateTime , nullable=False,unique=False)
    Student_id = db.Column(db.Integer,  db.ForeignKey(Student.id))
    Thread_id = db.Column(db.Integer,  db.ForeignKey(Thread.id))  

class Votes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    up_count = db.Column(db.Integer)
    down_count = db.Column(db.Integer)
    Student_id = db.Column(db.Integer,  db.ForeignKey(Student.id))
    Thread_id = db.Column(db.Integer,  db.ForeignKey(Thread.id))
    Posts_id = db.Column(db.Integer,  db.ForeignKey(Posts.id))  



class Subject(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name =db.Column(db.String(50),nullable = False , unique = False)
    year_no = db.Column(db.Integer)
    sem_no = db.Column(db.Integer)

class Upload(db.Model):
    upload_id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    Student_id = db.Column(db.Integer,  db.ForeignKey(Student.id))
    subject_id =db.Column(db.Integer,  db.ForeignKey(Subject.id))
  
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable = False , unique = False)
    description = db.Column(db.String(30),  nullable=False, unique=True)
    created = db.Column(db.String(100), nullable=False,unique=False)
    subject_id =db.Column(db.Integer,  db.ForeignKey(Subject.id))
    
class groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),  nullable=False, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id))
