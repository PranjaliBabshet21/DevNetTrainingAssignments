import parse
import parse_dnac
if __name__ == '__main__':
    x1 = (parse.parseJSON('data\db.json'))
    x2 = (parse.parseXML('data\db.xml'))
    x3 = (parse.parseYML('data\db.yml'))
    res = (parse_dnac.parseJSON('data\dnac_devices.json'))
    print("account information:")
    for i in x1:
        print(i[0],':','paid:',i[1],'due:',i[2])
    for i in x2:
        print(i[0],':','paid:',i[1],'due:',i[2])
    for i in x3:
        print(i[0],':','paid:',i[1],'due:',i[2])
    for lis in res:
        for key in lis:
            print("-----")
            print("id:",lis["id"])
            print("type:",lis['type'])
            print("family:",lis['family'])
            print("softwareType:",lis['softwareType'])
            print("mgmtIP:",lis['managementIpAddress'])