import requests

response_load = requests.post("http://localhost:3000/students", json=

{
    "name": "Siddanatham",
    "age": 27,
    "grade": "8th",
    "subjects": [
        "python",
        "selenium"
    ]

}
                              )
print(response_load)
print(type(response_load))
print(type(response_load.json()))
