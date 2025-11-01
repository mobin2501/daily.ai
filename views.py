from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Provider, Model, Conversation
from genai_client.gemini_client import GeminiClient
from genai_client.deepseek_client import DeepseekClient
from services import ConversationService

bp = Blueprint('main', __name__)

clients = {
    'gemini': GeminiClient(),
    'deepseek': DeepseekClient()
}

@bp.route('/')
def index():
    providers = Provider.query.filter_by(is_active=True).all()
    return render_template('index.html', providers=providers)

@bp.route('/admin')
def admin():
    providers = Provider.query.all()
    models = Model.query.all()
    return render_template('admin.html', providers=providers, models=models)

@bp.route('/admin/add-provider', methods=['POST'])
def add_provider():
    key = request.form.get('key')
    name = request.form.get('name')
    model_family = request.form.get('model_family')
    
    provider = Provider(key=key, name=name, model_family=model_family)
    db.session.add(provider)
    db.session.commit()
    
    return redirect(url_for('main.admin'))

@bp.route('/admin/add-model', methods=['POST'])
def add_model():
    provider_id = request.form.get('provider_id')
    name = request.form.get('name')
    model_id = request.form.get('model_id')
    is_default = request.form.get('is_default') == 'on'
    
    model = Model(
        provider_id=provider_id,
        name=name,
        model_id=model_id,
        is_default=is_default
    )
    db.session.add(model)
    db.session.commit()
    
    return redirect(url_for('main.admin'))


@bp.route('/admin/edit-provider/<int:provider_id>')
def edit_provider(provider_id):
    provider = Provider.query.get_or_404(provider_id)
    return render_template('edit_provider.html', provider=provider)

@bp.route('/admin/update-provider/<int:provider_id>', methods=['POST'])
def update_provider(provider_id):
    provider = Provider.query.get_or_404(provider_id)
    provider.key = request.form.get('key')
    provider.name = request.form.get('name')
    provider.model_family = request.form.get('model_family')
    provider.is_active = request.form.get('is_active') == 'on'
    db.session.commit()
    return redirect(url_for('main.admin'))

@bp.route('/admin/delete-provider/<int:provider_id>', methods=['POST'])
def delete_provider(provider_id):
    provider = Provider.query.get_or_404(provider_id)
    Model.query.filter_by(provider_id=provider_id).delete()
    db.session.delete(provider)
    db.session.commit()
    return redirect(url_for('main.admin'))

@bp.route('/admin/edit-model/<int:model_id>')
def edit_model(model_id):
    model = Model.query.get_or_404(model_id)
    providers = Provider.query.all()
    return render_template('edit_model.html', model=model, providers=providers)

@bp.route('/admin/update-model/<int:model_id>', methods=['POST'])
def update_model(model_id):
    model = Model.query.get_or_404(model_id)
    model.provider_id = request.form.get('provider_id')
    model.name = request.form.get('name')
    model.model_id = request.form.get('model_id')
    model.is_default = request.form.get('is_default') == 'on'
    model.is_active = request.form.get('is_active') == 'on'
    db.session.commit()
    return redirect(url_for('main.admin'))

@bp.route('/admin/delete-model/<int:model_id>', methods=['POST'])
def delete_model(model_id):
    model = Model.query.get_or_404(model_id)
    db.session.delete(model)
    db.session.commit()
    return redirect(url_for('main.admin'))

@bp.route('/chat', methods=['POST'])
def chat():
    prompt = request.form.get('prompt', '')
    model_id = request.form.get('model_id')
    
    model = Model.query.get(model_id)
    provider = model.provider
    
    # Get appropriate client based on provider key
    if provider.key == 'gemini':
        from genai_client.gemini_client import GeminiClient
        client = GeminiClient()
    elif provider.key == 'deepseek':
        from genai_client.deepseek_client import DeepseekClient
        client = DeepseekClient()
    
    response = client.generate(prompt, model.model_id)
    
    # Save with model_id instead of model_family
    ConversationService.save_conversation(prompt, response, model_id=model.id)
    
    return render_template('response.html', 
                         prompt=prompt, 
                         response=response, 
                         client=provider.name, 
                         model=model.model_id)
    
    
@bp.route('/conversations')
def conversations():
    conversations = Conversation.query.order_by(Conversation.created_at.desc()).all()
    return render_template('conversations.html', conversations=conversations)