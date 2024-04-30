import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the API key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Create a new model
model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

# initialize chat history
chat = model.start_chat(history=[])

print("Gemini です。何か質問ありますか？（終了するには、'/end'と入力してください")

# Chat Loop...
while True:
    # Get user input
    user_input = input("質問内容を入力してください：")

    # Check if user wants to quit
    if user_input == "/end":
        print("チャットを終了します。また質問してください。")
        break

    # Send user input to the model
    response = chat.send_message(user_input)

    # Print the model's response
    print(response.text)
