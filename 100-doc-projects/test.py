import requests

response = requests.get("https://api.github.com")
response.raise_for_status()  # Should print 200 if the request was successful

data = response.json()  # Convert the response to JSON format
print(data)  # Print the JSON data