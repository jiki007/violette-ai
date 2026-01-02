import asyncio
from rich.console import Console
from brain import start_chat, send_message_to_violette
from voice import violette_speak

console = Console()

async def main():
    chat = start_chat()
    
    # 1. State Variable: Voice is muted by default
    voice_active = False 

    console.clear()
    console.print("[bold magenta]Violette[/bold magenta]: I am online, Major. (Voice: [red]OFF[/red])\n")
    console.print("[dim]Tip: Type '/speak' to enable voice, '/quiet' to mute.[/dim]\n")

    while True:
        # Get input and strip whitespace
        user_input = console.input("[bold cyan]You[/bold cyan]: ").strip()

        # --- 🛡️ THE SAFETY CHECK ---
        # If the user just hits "Enter" (empty string), we skip everything.
        # This prevents the "Infinite Loop" that ate your quota!
        if not user_input:
            continue

        # --- COMMANDS ---
        if user_input.lower() in ("exit", "quit", "bye"):
            console.print("[bold magenta]Violette[/bold magenta]: Goodbye, Major.")
            break
            
        # Toggle Voice ON
        if user_input.lower() == "/speak":
            voice_active = True
            console.print("[italic green]Voice system activated. I will now speak aloud.[/]\n")
            continue 

        # Toggle Voice OFF
        if user_input.lower() == "/quiet":
            voice_active = False
            console.print("[italic yellow]Voice system muted.[/]\n")
            continue 

        # --- CHAT LOGIC ---
        try:
            with console.status("[bold magenta]Thinking...[/bold magenta]", spinner="dots"):
                response = send_message_to_violette(chat,user_input)
                
            console.print(f"[bold magenta]Violette[/bold magenta]: {response.text}\n")

            # Only speak if the toggle is ON
            if voice_active:
                await violette_speak(response.text)

        except Exception as e:
            console.print(f"[bold red]System Error:[/bold red] {e}")

if __name__=="__main__":
    asyncio.run(main())