import requests

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=54.9&longitude=23.9&current_weather=true")

print(response.status_code)
data = response.json()

print(data["current_weather"]["windspeed"])
print(data["current_weather_units"]["temperature"])

assert response.status_code == 200
assert data["current_weather"]["temperature"] > -60
expected = "°C"
unit = data["current_weather_units"]["temperature"]
assert unit == expected, f"Expected {expected}, got {unit}"
print("all checks passed")
