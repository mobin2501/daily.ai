from google import genai
from config import GEMINI_API_KEY
import markdown

class GeminiClient:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
    
    def generate(self, prompt, model_id):
        response = self.client.models.generate_content(
            model=model_id,  # Use string directly, not .value
            contents=prompt,
        )
        return markdown.markdown(response.text)