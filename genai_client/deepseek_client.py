from openai import OpenAI
from config import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL

class DeepseekClient:
    def __init__(self):
        self.client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)
    
    def generate(self, prompt, model_id):
        response = self.client.chat.completions.create(
            model=model_id,  # Use string directly
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )
        return response.choices[0].message.content