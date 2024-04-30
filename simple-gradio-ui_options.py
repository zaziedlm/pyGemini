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
        'temperature': temperature,
        'top_p': top_p,
        'top_k': top_k,
        'max_output_tokens': max_output_token
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

def on_reset():
    global in_session, chat
    in_session = False
    chat = None
    print("Chat session has been reset.")

if __name__ == '__main__':

    # initialize a chat session
    in_session = False
    chat = None

    # Gradio UI for Gemini Chatbot. model config slider set.
    model_options = [
        gr.Slider(label="Temperature", minimum=0, maximum=1, step=0.1, value=0.4, interactive=True),
        gr.Slider(label="Top-P", minimum=0.1, maximum=1, step=0.1, value=1, interactive=True),
        gr.Slider(label="Top-K", minimum=1, maximum=40, step=1, value=32, interactive=True),
        gr.Slider(label="Max Output Token", minimum=1, maximum=2048, step=1, value=1024, interactive=True),
    ]

    with gr.Blocks() as app:

        # Exec chatBot call function'gemini_chat'
        gr.ChatInterface(
            fn=gemini_chat,
            title="Gemini Chatbot",
            additional_inputs=model_options,
        )#.launch()

        # Gradio UI:reset session button set.
        session_button = gr.Button("Reset conversation history,session.（Note: Not synchronized with the Clear button)")

        # Reset button Listener.    
        session_button.click(fn=on_reset)
    app.launch()