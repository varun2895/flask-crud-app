import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.put(BASE + "video/1000", {'name':'amir','views':1000,'likes':99999999})

response = requests.delete(BASE + "video/1000")

print(response.json())