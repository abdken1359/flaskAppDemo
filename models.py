from app import db
class Person(db.Model):
    __tablename__="People"
    pid=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text,nullable=False)
    age=db.Column(db.Integer,nullable=False)
    job=db.Column(db.Text,nullable=False)
    def __repr__(self):
        return f"{self.name} is {self.age} years old, and is a {self.job}. "