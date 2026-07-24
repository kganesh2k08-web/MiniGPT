from google import genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read API key
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env")

# Create Gemini Client
client = genai.Client(
    api_key=API_KEY
)