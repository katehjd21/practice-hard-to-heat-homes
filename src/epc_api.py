import json
import urllib.request
from src.variables import EPC_BASE_URL
import requests

def epc_api_call(headers, params):

    full_url = f'{EPC_BASE_URL}{params}'

    try:
        # with urllib.request.urlopen(urllib.request.Request(full_url, headers=headers)) as response:
        #     response_body = response.read()

        #     if len(response_body) > 0:
        #         return json.loads(response_body)
        #     else: return {}

        response = requests.get(full_url, headers=headers)
        data = response.json()
        return data
    except Exception:
        return False