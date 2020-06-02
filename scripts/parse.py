import json
import xml.etree.ElementTree as ET 
import yaml

def parseJSON(filename):
    out1 = []
    with open(filename) as file:
        jdata = json.load(file)
    for key in jdata:
        out1.append((key,jdata[key]["paid"],jdata[key]["due"]))
    return out1

def parseXML(filename):  
    out2 = []
    tree = ET.parse(filename) 
    root = tree.getroot() 
    for ele in root:
        out2.append((ele.tag,ele[0].text,ele[1].text))
    return out2

def parseYML(filename):
    out3 = []
    with open(filename) as file:
        documents = yaml.full_load(file)
    for item, doc in documents.items():
        out3.append((item,doc["paid"],doc["due"]))
    return out3


    
