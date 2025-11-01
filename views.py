from flask import Blueprint, render_template, request
from genai_client.gemini_client import GeminiClient
from services import ConversationService
from models import Conversation

bp = Blueprint('main', __name__)
gemini_client = GeminiClient()

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/chat', methods=['POST'])
def chat():
    prompt = request.form.get('prompt', '')
    response = gemini_client.generate(prompt)
    
    ConversationService.save_conversation(prompt, response)
    
    return render_template('response.html', prompt=prompt, response=response)


@bp.route('/conversations')
def conversations():
    conversations = Conversation.query.order_by(Conversation.created_at.desc()).all()
    return render_template('conversations.html', conversations=conversations)