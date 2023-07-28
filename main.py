import requests

url = 'https://petstore.swagger.io/v2/user/123123'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
    "id": 123,
    "username": "avaliable",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
