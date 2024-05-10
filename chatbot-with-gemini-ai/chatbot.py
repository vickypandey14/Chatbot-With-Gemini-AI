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

    def _construct_message(self, text):
        """Construct a message for conversation history."""
        return {"text": text}

    def start_conversation(self):
        """Start a conversation and store conversation history."""
        self.conversation = self.model.start_chat(history=self._conversation_history)
        self._conversation_history.append(self._construct_message("Conversation started."))

    def get_response(self, user_input):
        """Get response from the chatbot."""
        if not self.conversation:
            raise GenAIException("Conversation not started.")
        response = self.model.continue_chat(self.conversation, user_input)
        self._conversation_history.append(self._construct_message(user_input))
        self._conversation_history.append(self._construct_message(response))
        return response

    def preload_conversation(self, conversation_history=None):
        """Preload conversation with history."""
        if conversation_history is not None and isinstance(conversation_history, list):
            self._conversation_history = conversation_history
        else:
            self._conversation_history = [
                self._construct_message('From now on, return the output as a JSON object that can be loaded in python with the key as \'text\'. For example, {"text": "<output goes here>"}'),
                self._construct_message('Sure, I can return the output as a regular JSON object with the key as `text`. Here is an example: {"text": "Your output"}.')
            ]