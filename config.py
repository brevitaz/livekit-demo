import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    AZURE_SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
    AZURE_SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION")
    AZURE_VOICE = os.getenv("AZURE_VOICE")
    USER_AWAY_TIMEOUT = os.getenv("USER_AWAY_TIMEOUT", 30.0)
    LLM_MODEL = os.getenv("LLM_MODEL", default="gpt-4o-mini")
    LLM_TEMPERATURE = os.getenv("LLM_TEMPERATURE", default=1.0)
    GROQ_LLM_MODEL = os.getenv("GROQ_LLM_MODEL", default="openai/gpt-oss-120b")
