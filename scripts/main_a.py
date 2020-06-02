import post
import get
import json

if __name__ == "__main__":
    token = post.get_token("https://sandboxdnac2.cisco.com/api/system/v1/auth/token")
    res = get.get_data("https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device",token)
    
    res = res["response"]
    for lis in res:
        for key in lis:
            print("-----")
            print("id:",lis["id"])
            print("type:",lis['type'])
            print("family:",lis['family'])
            print("softwareType:",lis['softwareType'])
            print("mgmtIP:",lis['managementIpAddress'])
    