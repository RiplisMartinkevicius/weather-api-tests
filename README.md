# Weather API Test Suite

A small pytest suite testing the Open-Meteo weather API (https://open-meteo.com/), written while relearning Python.

## What it tests
- Response status code and that data comes back in the expected shape
- Temperature values and units are sane
- Invalid input is rejected correctly (bad latitude, missing parameters)
- Boundary values for latitude (90 valid, 90.1 rejected)

## How to run it

pip install requests pytest
python -m pytest -v


Note: tests hit the live API, so they need an internet connection and can occasionally fail due to network timing rather than a real bug.
