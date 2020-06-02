import requests
import json
def get_token(url):
    #url = "https://sandboxdnac2.cisco.com/api/system/v1/auth/token"
    payload = {}
    headers = {
    'Authorization': 'Basic ZG5hY2RldjpEM3Y5M1RAd0sh'
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    data = json.loads(response.text.encode('utf8'))
    return data["Token"]