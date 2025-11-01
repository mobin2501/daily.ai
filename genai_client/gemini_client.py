from google import genai
from config import GEMINI_API_KEY, GeminiModels
import markdown

class GeminiClient:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
    
    def generate(self, prompt, gemini_model=GeminiModels.FLASH_20_LITE):
        response = self.client.models.generate_content(
            model=gemini_model.value,
            contents=prompt,
        )
        return markdown.markdown(response.text)