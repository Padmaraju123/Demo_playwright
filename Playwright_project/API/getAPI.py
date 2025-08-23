# api url
import json

import requests

response = requests.get("http://localhost:3000/students")

# here it will gives status value only
    # print(response)
    # print(type(response))

# # if you want content text
    # print(response.text)
    # print(type(response.text))

# convert the string value of response.text into dictionary by using json.loads

    # dic = json.loads(response.text)
    # print(dic)
    # print(type(dic))

# instead of above stuff we have direct solution to convert
json_format = response.json()
print(json_format)
print(type(json_format))

# to get the status code
status_code = response.status_code
assert status_code == 200
print(status_code)
print(type(status_code))

# to get the headers data
headers_data = response.headers
print(headers_data)
print(type(headers_data))

# getting the value of content-type in headers
# content_type = headers_data["Content-Type"]
# print(content_type)
# assert content_type == "application/json; charset=utf-8"
#
# # accessing the particular value in the response
# print(json_format["data"][0]["email"])

