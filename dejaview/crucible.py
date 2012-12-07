import requests

class Crucible(object):
    def __init__(self, baseurl):
        self.baseurl = baseurl

    def get_auth_token(username, password):
        request = get_auth_token_request(username, password)

    @staticmethod
    def get_auth_token_request(username, password):
        return {
            'url': '/rest-service/auth-v1/login',
            'parameters': {
                'userName': username,
                'password': password
            }
        }
