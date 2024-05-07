import google.generativeai as genai

class GenAIException(Exception):
    """GenAI Exception Base Class"""

class ChatBot:
    """ chat can only have one candidate count """
    CHATBOT_NAME = 'Byte Reptor'