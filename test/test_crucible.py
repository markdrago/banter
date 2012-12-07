import unittest

from dejaview import crucible

class TestRequest(unittest.TestCase):
    def setUp(self):
        self.c = crucible.Crucible('http://base/dir')

    def test_create_auth_request(self):
        r = self.c.get_auth_token_request('myuser', 'mypass')
        self.assertEqual('/rest-service/auth-v1/login', r['url'])
        self.assertEqual('myuser', r['parameters']['userName'])
        self.assertEqual('mypass', r['parameters']['password'])
