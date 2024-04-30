# Gemini API のスタートガイド: Python # Generative API のチュートリアル 
# https://ai.google.dev/gemini-api/docs/get-started/python?hl=ja

import google.generativeai as generativeai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the API key
generativeai.configure(api_key=os.getenv("GEMINI_API_KEY"))

gemini = generativeai.GenerativeModel('models/gemini-1.5-pro-latest')

# Set the prompt
prompt = "こんにちは、あなたは Gemini Proですか？"

# Generate a response
response = gemini.generate_content(prompt)

# Print the response
print(response.text)    # A quick accessor equivalent to self.candidates[0].content.parts[0].text


