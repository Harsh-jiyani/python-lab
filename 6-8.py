# Simple Chatbot
print("Hi, I'm PyBot! Ask me something or type 'bye' to exit.")

while True:
    user = input("You: ").lower()
    if "name" in user:
        print("PyBot: I'm just a friendly Python bot!")
    elif "age" in user:
        print("PyBot: I'm timeless :)")
        print("PyBot: Can you ask something else?")
        print("PyBot: Or type 'bye' to exit.")
    elif "ok" in user:
        print("PyBot: I'm here to help!")
    elif "bye" in user:
        print("PyBot: Goodbye!")
        break
    else:
        print("PyBot: Hmm, I don't understand that.")
        
    
     