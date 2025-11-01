from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()

class MessageType(enum.Enum):
    PROMPT = "prompt"
    RESPONSE = "response"

class ModelFamily(enum.Enum):
    GEMINI = "gemini"
    OPENAI = "openai"
    GROK = "grok"
    CLAUDE = "claude"
    LLAMA = "llama"

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
    model_family = db.Column(db.Enum(ModelFamily))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)