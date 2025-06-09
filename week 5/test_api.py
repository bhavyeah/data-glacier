import requests

# Replace with your deployed app URL
url = "https://iris-flower-app-bhavya-7ab98c1e8c35.herokuapp.com/api"

# Sample input: Sepal Length, Sepal Width, Petal Length, Petal Width
payload = {
    "features": [2.38, 5.21, 3.45, 2.45]
}

# Send POST request
response = requests.post(url, json=payload)

# Output the result
if response.status_code == 200:
    print("✅ Success:", response.json())
else:
    print("❌ Failed:", response.status_code, response.text)

