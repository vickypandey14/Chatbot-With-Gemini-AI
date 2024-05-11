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

        self.preload_conversation()

    def clear_conversations(self):
        self.conversation = self.model.start_chat(history=[])

    def start_conversation(self):
        self.conversation = self.model.start_chat(history=self._conversation_history)

    def _generation_config(self, temprature):
        return genai.types.GenerationConfig(
            temprature=temprature
        )

    def _construct_message(self, text, role='user'):
        return {
            'role': role,
            'parts': [text]
        }

    def preload_conversation(self, conversation_history=None):
        if isinstance(conversation_history, list):
            self._conversation_history = conversation_history
        else:
            self._conversation_history = [
                self._construct_message('From now on, return the output as a JSON object that can be loaded in python with the key as \'text\'. For example, {"text": "<output goes here>"}'),
                self._construct_message('Sure, I can return the output as a regular JSON object with the key as `text`. Here is an example: {"text": "Your output"}.')
            ]