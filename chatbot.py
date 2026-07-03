# Simple Rule-Based Chatbot

print("===== Simple Chatbot =====")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! Nice to meet you.")

    elif user == "hi":
        print("Bot: Hello!")

    elif user == "how are you":
        print("Bot: I am fine, thanks! How are you?")

    elif user == "i am fine":
        print("Bot: That's great to hear!")

    elif user == "what is your name":
        print("Bot: My name is Python Bot.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")