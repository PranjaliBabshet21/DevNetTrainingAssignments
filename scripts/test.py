import unittest
import parse
import parse_dnac

class Test(unittest.TestCase):
    def test_json(self):
        self.assertEqual(parse.parseJSON('data\db.json'),[('ACCT100', 60, 100), ('ACCT200', 70, 60), ('ACCT300', 0, 0)])
    def test_xml(self):
        self.assertEqual(parse.parseXML('data\db.xml'),[('ACCT400', '600', '10000'), ('ACCT500', '70', '40'), ('ACCT600', '0', '0')])
    def test_yml(self):
        self.assertEqual(parse.parseYML('data\db.yml'),[('ACCT700', 60, 100), ('ACCT800', 70, 60), ('ACCT900', 0, 0)])
    def test(self):
        self.assertEqual(list,type(parse_dnac.parseJSON('data\dnac_devices.json')))
if __name__=='__main__':
      unittest.main()
  