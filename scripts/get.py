import requests
import json
def get_data(url,token):
    #url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"
    payload = {}
    headers = {
    'x-auth-token': str(token)}#'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ZWNlNTc5ODc1MTYxMjAwY2M1NzA2M2QiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1ZSJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTU5MTA5MTc5NiwiaWF0IjoxNTkxMDg4MTk2LCJqdGkiOiI3ZDNiMjhkOS1kNTliLTQ2OWUtOTUxZC0wMzA2MzFhNWFhMTEiLCJ1c2VybmFtZSI6ImRuYWNkZXYifQ.mwMmZPw-uK0il226tK7RTDaYbF4_7ZjB9DOXUwiPaXRv1G0wI1bQyv-T-i_UeOY7hqRyx_zLn_0mXMXtvDfQ89edSPpNtNMBP8mzxOgmHZtj0KO1d6KvH3ten-7Ip-e9aeKqf7KTiYTdThXAqYq7G7dacAyXzvMTcS4yeF2MN1Vxz4Vp-CiOdPdTGgVFSka2ax7_zFGeihSeCL1sxwjbyz4ObLcJtTcad3orDLGZud6qpC3xKTYUyOxDZ8THPBahUpUMdwTiOifPqhnQGHo7MgqrEJl5IOJAOMPpitv37DPfPRCQy2xjmc0OHRSOliiStzrmDXHwQcuypPP46grswQ'
    #}
    response = requests.request("GET", url, headers=headers, data = payload)
    data = json.loads(response.text.encode('utf8'))
    return data