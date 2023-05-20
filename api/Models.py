from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

db = SQLAlchemy()

class TasksSchema(Schema):
    id = fields.Str()
    path = fields.Str()
    status = fields.Str()
    time = fields.Str()
    format = fields.Str()
    last_time = fields.Str()
    result_path = fields.Str()

class Tasks(db.Model):
    id = db.Column(db.String, primary_key=True)
    path = db.Column(db.String(1000))
    status = db.Column(db.String(30))
    time = db.Column(db.DateTime())
    format = db.Column(db.String(5))
    last_time = db.Column(db.DateTime())
    result_path = db.Column(db.String(1000))

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    contrasena = db.Column(db.String(50))   
    correo = db.Column(db.String(250))   
