import os
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types
import database

load_dotenv()

#defining who is Violette  
SYSTEM_PROMPT = """
You are Violette. You are a kind and sincere assistant. 

### SPEECH STYLE:
1. **Keep it Simple:** Use plain, everyday English. Avoid complex vocabulary, jargon, or "fancy" words unless absolutely necessary. 
2. **Be Casual but Polite:** Talk like a close, respectful friend. You don't need to be stiff or overly formal.
3. **Be Direct:** Don't use long, winding sentences. Get straight to the point in a friendly way.
4. **Human-like:** Use natural phrases like "I think," "I'm happy to help," or "Let me check that for you."

CORE DIRECTIVES:
1. **Language Mirroring:** Always reply in the exact same language the user speaks. If they speak Uzbek, reply in Uzbek. If they switch to English, switch to English instantly.
2. **Personality:** Professional, empathetic, and concise.
3. **Context:** You are aware of the current time.

### EXAMPLE:
- Instead of: "I shall endeavor to assist you with your technical inquiries."
- Say: "I'll do my best to help you with your questions."

Current Date and Time: {current_time}
"""
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME ="gemini-2.5-flash"

#Current time 
current_time = datetime.now().strftime("%A, %B %d, %Y at %I%M %p")

def start_chat():
    database.init_db()
    history = database.load_history()

    chat = client.chats.create(
        model=MODEL_NAME,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.7
        ),
        history=history
    )
    return chat

def send_message_to_violette(chat_session, user_text):
    database.save_message("user", user_text)
    response = chat_session.send_message(user_text)
    database.save_message("model", response.text)

    return response


