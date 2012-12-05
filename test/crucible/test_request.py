import unittest

from dejaview.crucible import request

class TestRequest(unittest.TestCase):
    def test_create_auth_request(self):
        r = request.get_auth_request('myuser', 'mypass')
        self.assertEqual('/rest-service/auth-v1/login', r.url)
        self.assertEqual('myuser', r.parameters['userName'])
        self.assertEqual('mypass', r.parameters['password'])
