# Daily.AI

**Setup Instructions:**

1. **Clone and navigate to project:**
```bash
git clone <repo-url>
cd daily.ai
```

2. **Create virtual environment with pyenv and activate:**
```bash
pyenv virtualenv 3.12.12 llm  # or your Python version
pyenv activate llm
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create `.env` file in root:**
```
GEMINI_API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
```

5. **Configure Alembic (alembic.ini):**
Ensure this line is set:
```ini
sqlalchemy.url = sqlite:///instance/app.db
```

6. **Run database migrations:**
```bash
alembic upgrade head
```
This creates `instance/app.db` with all tables.

7. **Run the application:**
```bash
python app.py
```

8. **Access the app:**
- Main chat: `http://localhost:5000`
- View conversations: `http://localhost:5000/conversations`

**Project Structure:**
```
daily.ai/
├── alembic/           # Database migrations
├── genai_client/      # Gemini API client
├── templates/         # HTML templates
├── instance/          # Database location (created automatically)
│   └── app.db        # SQLite database
├── app.py            # Main Flask app
├── models.py         # Database models
├── views.py          # Routes
├── services.py       # Business logic
├── config.py         # Configuration
├── alembic.ini       # Alembic config
├── requirements.txt  # Dependencies
├── .env              # Environment variables (not in git)
└── README.md
```

## Quick Links

### Generative AI

- <a href="https://chat.openai.com/" target="_blank">ChatGPT</a>
- <a href="https://claude.ai/" target="_blank">Claude</a>
- <a href="https://gemini.google.com/app" target="_blank">Gemini</a>
- <a href="https://chat.mistral.ai/chat" target="_blank">Mistral AI</a>
- <a href="https://grok.com/" target="_blank">Grok</a>
- <a href="https://chat.deepseek.com/" target="_blank">Deepseek</a>
