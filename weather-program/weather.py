import requests

API_KEY = "b0f9af17401a09a6c552dfbe1318005c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("The weather feels like", weather)
    temp = round(data['main']['temp'] - 273)
    print("The current tempeture is", temp, "ºC")

else:
    print("An error occurred")