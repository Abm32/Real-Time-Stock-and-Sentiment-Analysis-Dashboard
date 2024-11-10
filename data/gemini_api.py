import requests
from config import GEMINI_API_KEY

def get_real_time_price(symbol):
    url = f'https://api.gemini.com/v1/pubticker/{symbol}'
    headers = {"X-GEMINI-APIKEY": GEMINI_API_KEY}
    response = requests.get(url, headers=headers)
    
    # Return data if successful, else None
    if response.status_code == 200:
        return response.json()
    else:
        return None
