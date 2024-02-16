import re

def simple_chatbot(user_input):
   
    user_input = user_input.lower()

    
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hi there! How can I help you?"

    elif re.search(r'\b(how are you|how\'s it going)\b', user_input):
        return "I'm just a chatbot, but thanks for asking!"

    elif re.search(r'\b(bye|goodbye)\b', user_input):
        return "Goodbye! Have a great day!"

    elif re.search(r'\b(thank you|thanks)\b', user_input):
        return "You're welcome!"

    elif re.search(r'\b(what is your name|who are you)\b', user_input):
        return "I'm a simple chatbot. You can call me ChatGPT."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():hi
print("Welcome to the Simple Chatbot!")

while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye! Have a great day!")
            break

        response = simple_chatbot(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
