import json
import xml.etree.ElementTree as ET 
import yaml
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list,type(parseJSON('db.json')))
        self.assertEqual(list,type(parseXML('db.xml')))
        self.assertEqual(list,type(parseYML('db.yml')))

def parseJSON(jsonfile):
    out1 = []
    with open(jsonfile) as fj0:
        jdata = json.load(fj0)
    for key in jdata:
        print(key,":","paid :",jdata[key]["paid"],"due :",jdata[key]["due"])
        out1.append((jdata[key]["paid"],jdata[key]["due"]))
    return out1

def parseXML(xmlfile):  
    out2 = []
    tree = ET.parse(xmlfile) 
    root = tree.getroot() 
    for ele in root:
        print(ele.tag,":",ele[0].tag,":",ele[0].text,ele[1].tag,":",ele[1].text)
        out2.append(([ele[0].text,ele[1].text]))
    return out2

def parseYML(ymlfile):
    out3 = []
    with open(ymlfile) as file:
        documents = yaml.full_load(file)
    for item, doc in documents.items():
        print(item, ":","paid :",doc["paid"],"due :",doc["due"])
        out3.append((doc["paid"],doc["due"]))
    return out3

x = Test()
x.test()

#parseJSON('db.json')
#parseXML('db.xml')
#parseYML('db.yml')