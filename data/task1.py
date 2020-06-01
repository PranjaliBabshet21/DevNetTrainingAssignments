import json
import xml.etree.ElementTree as ET 
import yaml

def parseJSON(jsonfile):
    with open(jsonfile) as fj0:
        jdata = json.load(fj0)
    for key in jdata:
        print(key,":","paid :",jdata[key]["paid"],"due :",jdata[key]["due"])

def parseXML(xmlfile):  
    tree = ET.parse(xmlfile) 
    root = tree.getroot() 
    for ele in root:
        print(ele.tag,":",ele[0].tag,":",ele[0].text,ele[1].tag,":",ele[1].text)

def parseYML(ymlfile):
    with open(ymlfile) as file:
        documents = yaml.full_load(file)
    for item, doc in documents.items():
        print(item, ":","paid :",doc["paid"],"due :",doc["due"])

parseJSON('db.json')
parseXML('db.xml')
parseYML('db.yml')