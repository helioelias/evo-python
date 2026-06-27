import os
import json
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações da API
base_url = os.getenv("EVOLUTION_API_URL", "http://localhost:8080").rstrip('/')
url = f"{base_url}/instance/create"
api_key = os.getenv("EVOLUTION_API_KEY", "429683C4C977415CAAFCCE10F7D57E11")

# Configurações da instância
instance_name = os.getenv("EVOLUTION_INSTANCE_NAME", "ebainstance")
qrcode = os.getenv("EVOLUTION_INSTANCE_QRCODE", "true").lower() in ("true", "1", "yes")
mobile = os.getenv("EVOLUTION_INSTANCE_MOBILE", "false").lower() in ("true", "1", "yes")
integration = os.getenv("EVOLUTION_INSTANCE_INTEGRATION", "WHATSAPP-BAILEYS")

payload = json.dumps({
  "instanceName": instance_name,
  "qrcode": qrcode,
  "mobile": mobile,
  "integration": integration
})

headers = {
  'Content-Type': 'application/json',
  'apikey': api_key
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)