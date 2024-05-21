import sys
from configparser import ConfigParser
from chatbot import ChatBot

def main():
    config = ConfigParser()
    config.read('credentials.ini')
    api_key = config['gemini_api']['API_KEY']

    chatbot = ChatBot(api_key=api_key)
    chatbot.start_conversation()
    # chatbot.clean_conversation()

    print("Hello! I'm Byte Reptor Chatbot. How can I assist you today? Type 'quit' to exit.")

    while True:
        user_input = input("you: ")
        if user_input.lower() == 'quit':
            # print("Exiting the chatbot. Goodbye!")

            sys.exit("Exiting the chatbot. Goodbye!")

        try:
            response = chatbot.send_prompt(user_input)
            print(f"{chatbot.CHATBOT_NAME}: {response}")
        except Exception as e:
            print(f"An error occurred: {e}")

main()