import requests
import json

url = "http://localhost:8080/instance/create"

payload = json.dumps({
  "instanceName": "ebainstance",
  #"token": "B6D711FCDE4D4FD5936544120E713976",
  "qrcode": True,
  "mobile": False,
  "integration": "WHATSAPP-BAILEYS"
})
headers = {
  'Content-Type': 'application/json',
  'apikey': '429683C4C977415CAAFCCE10F7D57E11'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
print(response.text)