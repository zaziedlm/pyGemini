# Gemini API のスタートガイド: Python # Generative API のチュートリアル 
# https://ai.google.dev/gemini-api/docs/get-started/python?hl=ja
# 新しい Gemini API クックブック
# https://github.com/google-gemini/cookbook?tab=readme-ov-file#welcome-to-the-gemini-api-cookbook

import google.generativeai as generativeai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the API key
generativeai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#gemini = generativeai.GenerativeModel('models/gemini-1.5-pro-latest')

#model_name = 'models/gemini-1.5-pro-latest'
model_name = 'models/gemini-1.5-flash'
gemini = generativeai.GenerativeModel(model_name)


# Set the prompt
prompt = "こんにちは、あなたのモデル名は、Gemini Proですか？出来るだけ正確なモデル名を教えてください"

# Generate a response
response = gemini.generate_content(prompt)

# Print the response
print(response.text)    # A quick accessor equivalent to self.candidates[0].content.parts[0].text


