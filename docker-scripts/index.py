#!/usr/bin/python3
print("Content-Type:text/html")
print("")

import cgi,cgitb
cgitb.enable() # Enable debugging
print("<h1>Below is the execution output of the script</h1>")
print("------------------------------------<br>")

##-------PASTE YOUR SCRIPT BELOW---------#######

import post
import get
import json

if __name__ == "__main__":
    token = post.get_token("https://sandboxdnac2.cisco.com/api/system/v1/auth/token")
    res = get.get_data("https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device",token)
    res = res["response"]
    for lis in res:
        for key in lis:
            print("<h1>-----</h1>")
            print("<h3>id:",lis["id"],"</h3>")
            print("<h3>type:",lis['type'],"</h3>")
            print("<h3>family:",lis['family'],"</h3>")
            print("<h3>softwareType:",lis['softwareType'],"</h3>")
            print("<h3>mgmtIP:",lis['managementIpAddress'],"</h3>")