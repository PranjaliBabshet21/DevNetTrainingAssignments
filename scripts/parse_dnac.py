import json
def parseJSON(jsonfile):
    with open(jsonfile) as fj0:
        jdata = json.load(fj0)
    res = jdata["response"]
    return res