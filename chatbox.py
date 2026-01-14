import random

greetings = ["Hello! How can I help you?", "Hi there, what do you need?", "Hey! Ready to chat.", "Greetings!"]
farewells = ["Goodbye! Have a great day!", "See you later!", "Bye!"]

print("Chatbot: Hi! I am a simple rule-based chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Chatbot:", random.choice(greetings))
    elif user_input == "how are you?":
        print("Chatbot: I am just a program, but I'm doing well. Thank you!")
    elif user_input == "bye":
        print("Chatbot:", random.choice(farewells))
        break
    else:
        print("Chatbot: Sorry, I don't understand that specific query.")
