---
layout: default
title: Daily.AI - Multi-Model AI Chat Application
---

<div style="text-align: center; margin: 2rem 0;">
  <h1>🤖 Daily.AI</h1>
  <p style="font-size: 1.2rem; color: #666;">A Flask-based chat application with multiple AI model support</p>
</div>

---

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone https://github.com/mobin2501/daily.ai.git
cd daily.ai
```

### 2. Create Virtual Environment
```bash
pyenv virtualenv 3.12.12 llm
pyenv activate llm
pip install -r requirements.txt
```

### 3. Configure Environment
Create `.env` file:
```
GEMINI_API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
```

Ensure `alembic.ini` has:
```ini
sqlalchemy.url = sqlite:///instance/app.db
```

### 4. Initialize Database
```bash
alembic upgrade head
```

### 5. Run Application
```bash
python app.py
```

**Access at:**
- 💬 Main chat: [http://localhost:5000](http://localhost:5000)
- 📜 Conversations: [http://localhost:5000/conversations](http://localhost:5000/conversations)

---

## 📁 Project Structure
```
daily.ai/
├── alembic/           # Database migrations
├── genai_client/      # Gemini API client
├── templates/         # HTML templates
├── instance/          # Database (auto-generated)
│   └── app.db        # SQLite database
├── app.py            # Main Flask app
├── models.py         # Database models
├── views.py          # Routes
├── services.py       # Business logic
├── config.py         # Configuration
├── alembic.ini       # Alembic config
├── requirements.txt  # Dependencies
└── .env              # Environment variables
```

---

## 🔗 Quick Links - Generative AI Platforms

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 2rem 0;">
  <div style="border: 1px solid #ddd; padding: 1rem; border-radius: 8px; text-align: center;">
    <h3>ChatGPT</h3>
    <a href="https://chat.openai.com/" target="_blank">Visit →</a>
  </div>
  <div style="border: 1px solid #ddd; padding: 1rem; border-radius: 8px; text-align: center;">
    <h3>Claude</h3>
    <a href="https://claude.ai/" target="_blank">Visit →</a>
  </div>
  <div style="border: 1px solid #ddd; padding: 1rem; border-radius: 8px; text-align: center;">
    <h3>Gemini</h3>
    <a href="https://gemini.google.com/app" target="_blank">Visit →</a>
  </div>
  <div style="border: 1px solid #ddd; padding: 1rem; border-radius: 8px; text-align: center;">
    <h3>Mistral AI</h3>
    <a href="https://chat.mistral.ai/chat" target="_blank">Visit →</a>
  </div>
  <div style="border: 1px solid #ddd; padding: 1rem; border-radius: 8px; text-align: center;">
    <h3>Grok</h3>
    <a href="https://grok.com/" target="_blank">Visit →</a>
  </div>
  <div style="border: 1px solid #ddd; padding: 1rem; border-radius: 8px; text-align: center;">
    <h3>Deepseek</h3>
    <a href="https://chat.deepseek.com/" target="_blank">Visit →</a>
  </div>
</div>

---

<div style="text-align: center; margin-top: 3rem; color: #666;">
  <p>Made with ❤️ using Flask and AI</p>
</div>