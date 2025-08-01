import requests
import os
from dotenv import load_dotenv

load_dotenv()
# Load your API key from a .env file (create one with API_KEY=your_api_key)
api_key = os.getenv("API_KEY")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get("main"):
        temp_c = data["main"]["temp"]
        temp_f = (temp_c * 9/5) + 32
        print(f"Current temperature in {city}: {temp_c:.1f}°C / {temp_f:.1f}°F")
    else:
        print("City not found.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)

# Note:
# You must create a .env file in the same directory with the following content:
# API_KEY=your_openweathermap_api_key
#
# This key should NOT be committed to version control for security reasons.
