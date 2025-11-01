from dotenv import load_dotenv
from enum import Enum
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'

class GeminiModels(Enum):
    FLASH_20 = 'gemini-2.0-flash'
    FLASH_20_EXP = 'gemini-2.0-flash-exp'
    FLASH_20_LITE = 'gemini-2.0-flash-lite'
    FLASH_20_LIVE = 'gemini-2.0-flash-live'
    
    FLASH_25 = 'gemini-2.5-flash'
    FLASH_25_LITE = 'gemini-2.5-flash-lite'
    FLASH_25_LIVE = 'gemini-2.5-flash-live'
    
    PRO_25 = 'gemini-2.5-pro'