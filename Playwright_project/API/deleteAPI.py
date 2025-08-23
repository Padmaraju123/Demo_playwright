import requests

response_payload = requests.delete("http://localhost:3000/students/3")
print(response_payload.json())
