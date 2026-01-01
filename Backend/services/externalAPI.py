import requests
import os
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("API_KEY")

def call_foodAPI(food):
    query = food
    quantity = '100g'
    api_url = 'https://api.api-ninjas.com/v1/nutritionitem'
    response = requests.get(api_url, headers={'X-Api-Key': secret_key}, params={'query': query, 'quantity': quantity})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)

