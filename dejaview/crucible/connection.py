class Connection(object):
    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.conn = None

    def send_request(self, request):
        print 'send request to server'
