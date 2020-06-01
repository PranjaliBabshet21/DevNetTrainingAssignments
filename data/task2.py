import json

def parseJSON(jsonfile):
    with open(jsonfile) as fj0:
        jdata = json.load(fj0)
    res = jdata["response"]
    for lis in res:
        for key in lis:
            print("id:",lis["id"],"type:",lis['type'],"family:",lis['family'],"softwareType:",lis['softwareType'],"mgmtIP:",lis['managementIpAddress'])
parseJSON('dnac_devices.json')