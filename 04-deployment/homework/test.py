import requests

arg = {
    "year": 2023,
    "month": 5
}

response = requests.post('http://localhost:9696/predict',json=arg)

print(response.json())