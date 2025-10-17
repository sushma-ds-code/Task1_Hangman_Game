# Task 4: Basic Chatbot (Rule-Based)

def chatbot():
    print("Chatbot: Hi! I am your assistant. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for comparison
        
        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

# Run chatbot
chatbot()
