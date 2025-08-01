import requests

def get_weather(city):
    api_key = "your_api_key_here"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get("main"):
        temp = data["main"]["temp"]
        print(f"Current temperature in {city}: {temp}°C")
    else:
        print("City not found.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
