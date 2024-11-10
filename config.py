import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants for API keys and URIs
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DATABRICKS_API_KEY = os.getenv("DATABRICKS_API_KEY")

# Get MongoDB credentials
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
encoded_password = quote_plus(db_password)  # URL-encode the password

# Construct MongoDB URI
MONGODB_URI = f"mongodb+srv://{db_username}:{encoded_password}@cluster0.ulhjg2a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

print(MONGODB_URI)  # Optional: print to verify

# Now you can use MONGODB_URI to initialize your MongoDB client
