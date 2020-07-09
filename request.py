import requests

url = "http://localhost:5000/predict_api"
r = requests.post(url, json={"city":1, "area":213, "rooms":2, "bathroom":1, "parking spaces":1, "floor":2, "animal":1, "furniture":1})

print(r.json())


