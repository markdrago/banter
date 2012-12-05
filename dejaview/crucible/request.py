def get_auth_request(username, password):
    return Request(url='/rest-service/auth-v1/login',
                   parameters={'userName': username,
                               'password': password})

class Request(object):
    def __init__(self, url=None, parameters=None, data=None, method='GET'):
        self.url = url
        self.parameters = parameters
        self.data = data
        self.method = method
