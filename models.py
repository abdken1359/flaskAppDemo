from app import db
from flask_login import UserMixin
class Person(db.Model):
    __tablename__="People"
    pid=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text,nullable=False)
    age=db.Column(db.Integer,nullable=False)
    job=db.Column(db.Text,nullable=False)
    def __repr__(self):
        return f"{self.name} is {self.age} years old, and is a {self.job}. "
class User(db.Model,UserMixin):
    __tablename__="Users"
    uid=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,nullable=False)
    password=db.Column(db.String,nullable=False)
    role=db.Column(db.String)
    description=  db.Column(db.String)
    def __repr__(self):
        return f"<User:{self.username}, Role:{self.role}>"
    def get_id(self):
        return str(self.uid)

