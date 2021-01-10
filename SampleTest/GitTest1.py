import requests
import json


url = "http://localhost:8888/student/2"

payload={}
headers = {
  'Cookie': 'JSESSIONID.e0034da8=node0df7mlxqjh1pz1dn4bkw9lf7kw0.node0'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)