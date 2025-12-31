import asyncio
from rich.console import Console
from brain import start_chat
from voice import violette_speak

console = Console()

async def main():
    chat = start_chat()
    console.print("[bold magenta]Violette[/bold magenta]: I am online, Major. 🌸")

    while True:
        user_input = console.input("[bold cyan]You[/bold cyan]:".strip())

        if user_input.lower() in ("exit", "quit"):
            break
        
        with console.status("[bold magenta]Thinking....[/bold magenta]", spinner="dots"):
            response = chat.send_message(user_input)
        console.print(f"[bold magenta]Violette[/bold magenta]: {response.text}\n")

        #Speak the response
        await violette_speak(response.text)

if __name__=="__main__":
    asyncio.run(main())