def get_response(user_input):
    # Standardize input to lowercase and strip whitespace
    cleaned_input = user_input.lower().strip()

    # Define rule-based conditions
    if "hello" in cleaned_input or "hi" in cleaned_input:
        return "Hi! How can I help you today?"
    elif "how are you" in cleaned_input:
        return "I'm fine, thanks for asking!"
    elif "bye" in cleaned_input or "exit" in cleaned_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Could you try asking something else?"


def main():
    print("Chatbot: Hello! Type 'bye' to exit the chat.\n")

    # Continuous loop for conversation
    while True:
        user_input = input("You: ")

        # Get response using the function
        response = get_response(user_input)
        print(f"Chatbot: {response}\n")

        # Exit loop if user says bye/exit
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break


# Run the chatbot program
if __name__ == "__main__":
    main()