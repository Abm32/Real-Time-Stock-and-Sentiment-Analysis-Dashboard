import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants for API keys and URIs
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")
DATABRICKS_API_KEY = os.getenv("DATABRICKS_API_KEY")
