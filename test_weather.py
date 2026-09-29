import requests
import pytest

URL = "https://api.open-meteo.com/v1/forecast?latitude=54.9&longitude=23.9&current_weather=true"

@pytest.fixture
def weather_response():
    return requests.get(URL, timeout=10)

#check for json info
def test_status_code_is_200(weather_response):
    assert weather_response.status_code == 200


def test_temperature_unit_is_celsius(weather_response):
    data = weather_response.json()
    unit = data["current_weather_units"]["temperature"]
    assert unit == "°C", f"Expected °C, got {unit}"

def test_temperature_is_realistic(weather_response):
    data = weather_response.json()
    temperature = data["current_weather"]["temperature"]
    assert -60 < temperature < 60

#check for status code and error
def test_invalid_latitude():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=999&longitude=23.9&current_weather=true",
        timeout=10
    )
    assert response.status_code == 400
    body = response.json()
    assert body["error"] is True

def test_missing_longitude():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=54.9&current_weather=true",
        timeout=10
    )
    assert response.status_code == 400
    body = response.json()
    assert body["error"] is True

#boundary test
def test_90_latitude():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=90&longitude=23.9&current_weather=true",
        timeout=10
    )
    assert response.status_code == 200

def test_90_1_latitude():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=90.1&longitude=23.9&current_weather=true",
        timeout=10
    )
    assert response.status_code == 400