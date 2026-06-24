# Simple Rule-Based Chatbot Project
# Concepts Used: if-elif, functions, loops, input/output

def show_help():
    print("\nYou can try these commands:")
    print("- hello / hi")
    print("- how are you?")
    print("- what's your name?")
    print("- tell me a joke")
    print("- help")
    print("- bye / exit\n")


def tell_joke():
    print("Bot: Why don't programmers like nature?")
    print("Bot: Because it has too many bugs! 😂")


def chatbot():
    print("-" * 35)
    print("🤖 Welcome to Simple ChatBot")
    print("-" * 35)

    name = input("Bot: What's your name? ")
    print(f"Bot: Nice to meet you, {name}!")

    while True:
        user = input(f"\n{name}: ").lower().strip()

        if user in ["hello", "hi", "hey", "heyy"]:
            print(f"Bot: Hello {name}! 👋")

        elif user == "how are you?":
            print("Bot: I'm doing great! Thanks for asking. 😊")

        elif user == "what's your name?" or user == "who are you?":
            print("Bot: I'm Simples ChatBot, your virtual assistant.")

        elif user == "tell me a joke":
            tell_joke()

        elif user == "help":
            show_help()

        elif user in ["thank you", "thanks"]:
            print("Bot: You're welcome! 😄")

        elif user in ["bye", "exit", "quit"]:
            print(f"Bot: Goodbye {name}! Have a great day! 👋")
            break

        else:
            print("Bot: Sorry, I don't understand that.")
            print("Bot: Type 'help' to see available commands.")


# Run chatbot
chatbot()