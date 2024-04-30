import google.generativeai as genai
#from google.ai.generativelanguage import Content, Part
from google.ai import generativelanguage as glm
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Gemini chat function
def gemini_chat(message, gemini_history, temperature, top_p, top_k, max_output_token):

    # session valiable, global use!!
    global in_session, chat
    
    # Get the API key and secret from the environment variables
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

    # model configuration
    genaration_config = {
        'temperature': 0.4,
        'top_p': 1,
        'top_k': 32,
        'max_output_tokens': 1024
    }

    # create a model
    gemini_model = genai.GenerativeModel(
        model_name='gemini-pro',
        generation_config=genaration_config,
    )

    # # initialize a chat history
    # gemini_history = []

    # # add the user's message to the chat history
    # for row in history:
    #     input_from_user = row[0]
    #     output_from_gemini = row[1]

    #     gemini_history.append(glm.Content(role="user", parts=[glm.Part.from_text(input_from_user)]))
    #     gemini_history.append(glm.Content(role="model", parts=[glm.Part.from_text(output_from_gemini)]))  
    # add chat history to Gemini model 
    # gemini_history = []
    # chat = gemini_model.start_chat(history=gemini_history)
    
    # check session status. if in-session, new start_chat().
    # attension! Clear button will not clear the session, yet.
    if not in_session:
        chat = gemini_model.start_chat(history=[])
        # into multi-turn sesseion.
        in_session = True

    # send user's message to Gemini model
    try:
        response = chat.send_message(message).text

    except IndexError as e:
        print(f"Error: {e}")
        return "Gemini から応答ありませんでした。文章を変えてもう一度質問をしてください。"
    
    return response

import gradio as gr

if __name__ == '__main__':

    # initialize a chat session
    in_session = False
    chat = None

    # Exec chatBot call function'gemini_chat'
    gr.ChatInterface(
        fn=gemini_chat,
        title="Gemini Chatbot",
    ).launch()

