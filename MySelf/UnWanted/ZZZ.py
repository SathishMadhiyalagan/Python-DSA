import requests

url = 'http://127.0.0.1:5000/process'
data ={
  "text": "The rs."
}



# Use the json parameter to send JSON data
response = requests.post(url, json=data)

# Print the response text
print(response.text)

URL = "http://127.0.0.1:5000/history"
r = requests.get(url = URL)

data = r.json()

print(data)