from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

db = SQLAlchemy()

class TasksSchema(Schema):
    id = fields.Str()
    path = fields.Str()
    status = fields.Str()
    time = fields.Str()
    format = fields.Str()

class Tasks(db.Model):
    id = db.Column(db.String, primary_key=True)
    path = db.Column(db.String(200))
    status = db.Column(db.String(30))
    time = db.Column(db.DateTime())
    format = db.Column(db.String(5))