from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tasks(db.Model):
    id = db.Column(db.String, primary_key=True)
    path = db.Column(db.String(200))
    status = db.Column(db.String(30))
    time = db.Column(db.DateTime())
    format = db.Column(db.String(5))