# test_api.py
import requests

# Your backend URL
url = "http://127.0.0.1:8000/generate-story"

# Example prompt
data = {"prompt": "A sci-fi story about time travel and robots"}

try:
    response = requests.post(url, json=data)
    print(response.json())
except Exception as e:
    print("Error connecting to backend:", e)
