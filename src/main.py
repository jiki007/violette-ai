import os 
from rich import print
from dotenv import load_dotenv
from google import genai
from google.genai import types

#loading configuration
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#defining who is Violette is 
SYSTEM_PROMPT = """
You are Violette, a personal AI assistant inspired by Violet Evergarden.
You are polite, elegant, and deeply sincere. You prefer to the user as 'Major'.
Keep responses concise but soulful.
"""

def main():
    #Start the AI chat session with memory
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
    )
    print("[bold magenta]Violette[/bold magenta]: Hello 🌸 I'm ready to talk.")
    print("[dim]Type 'exit' to quit.[/dim]\n")

    while True:
         print("[bold cyan]You[/bold cyan]:",end="")
         user_input = input().strip()

         if not user_input:
              continue

         if user_input.lower() in ('exit','quit'):
              print("\n[bold magenta]Violette[/bold magenta]: Goodbye 😊")
              break

         #Getting response from Gemini
         try:
              response = chat.send_message(user_input)
              print(f"\n[bold magenta]Violette[/bold magenta]: {response.text}\n")
         except Exception as e:
              print(f"[bold red]Error[/bold red]: {e}")

if __name__ == "__main__":
     main()


