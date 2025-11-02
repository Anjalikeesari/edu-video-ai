import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
TRANSCRIPTION_MODEL = os.getenv("TRANSCRIPTION_MODEL", "whisper")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///dev.db")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
