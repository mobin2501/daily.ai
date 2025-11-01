from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()

class MessageType(Enum):
    PROMPT = "prompt"
    RESPONSE = "response"


class Provider(db.Model):
    __tablename__ = 'provider'
    
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)  # 'gemini', 'deepseek'
    name = db.Column(db.String(100), nullable=False)  # 'Google Gemini'
    model_family = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    models = db.relationship('Model', backref='provider', lazy=True)


class Model(db.Model):
    __tablename__ = 'model'
    
    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)  
    model_id = db.Column(db.String(100), nullable=False)  # 'gemini-2.0-flash'
    is_default = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)


class Conversation(db.Model):
    __tablename__ = 'conversation'
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    messages = db.relationship('Message', backref='conversation', lazy=True)


class Message(db.Model):
    __tablename__ = 'message'
    
    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'), nullable=False)
    type = db.Column(db.Enum(MessageType), nullable=False)
    content = db.Column(db.Text, nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable=True)
    model = db.relationship('Model', backref='messages', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)