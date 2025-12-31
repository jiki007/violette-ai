from rich import print

def main():
    print("[bold magenta]Violette[/bold magenta]: Hello 🌸 I'm ready to talk.")
    print("[dim] Type 'exit' to quit.[/dim]\n")

    while True:
        print("[bold cyan]You[/bold cyan]: ", end="")
        user_input = input().strip()

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("\n[bold magenta]Violette[/bold magenta]: Goodbye 🌙")
            break

        print(f"[bold magenta]Violette[/bold magenta]: You said -> {user_input}")


if __name__ == "__main__":
    main()
