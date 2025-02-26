from app import db

class ToDo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    task = db.Column(db.String(100), nullable=False)