import google.generativeai as genai

class GenAIException(Exception):
    """GenAI Exception Base Class"""

class ChatBot:
    """ chat can only have one candidate count """
    CHATBOT_NAME = 'Byte Reptor'

    def __init__(self, api_key):
        self.genai = genai
        self.genai.configure(api_key=api_key)
        self.model = self.genai.GenerativeModel('gemini-pro')
        self.conversation = None
        self._conversation_history = []

    def start_conversation(self):
        self.conversation = self.model.start_chat(history=self._conversation_history)

    def preload_conversation(self, conversation_history=None):
        if isinstance(conversation_history, list):
            self._conversation_history = conversation_history
        else:
            self._conversation_history = [
                self._construct_message('Hello, how can I assist you today?')


            ]