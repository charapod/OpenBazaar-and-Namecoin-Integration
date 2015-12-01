class TestDNSChainLookup(unittest.TestCase):

    def setUp(self):
        self.dnschain_server = Server(
            "192.184.93.146",
            "NOTYETIMPLEMENTED"
        )
        self.test_cases = {
            "id/dionyziz": "dionyziz@gmail.com",
            "id/greg": ["contact@taoeffect.com",
                        "hi@okturtles.com"]
        }
        self.responses = {}
        for name in self.test_cases:
            self.responses[name] = \
                self.dnschain_server.lookup(name)
        
    def test_valid_JSON(self):
        for response in self.responses.itervalues():
            try:
                json.dumps(response)
            except:
                self.fail("Response was not valid JSON")
        
    def test_contains_email(self):
        for response in self.responses.itervalues():
            self.assertIn("email", response)

    def test_correct_email(self):
        for name in self.test_cases:
            if "email" not in self.responses[name]:
                self.skipTest(
                    'Response does not contain key "email"'
                )
            self.assertEqual(self.test_cases[name], 
                             self.responses[name]["email"])
