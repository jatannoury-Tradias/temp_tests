import requests
import config

ENVIRONMENT = 'otcweb-uat'
PROTOCOL = 'https'
headers = {'Content-Type': 'application/json',  'Accept': 'application/json',  'Authorization': f'Bearer {config.UAT_TOKEN2}'}
r = requests.get(f'{PROTOCOL}://{ENVIRONMENT}.tradias.de/api/settlement-requests', headers = headers,json={
  "client_settlement_request_id": "string",
  "trade_ids": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "request_amounts": [
    {
      "currency": "string",
      "from_address": "string",
      "to_address": "string",
      "amount": 0
    }
  ]
})
# print(r.json())