import requests
import urlparse
import json

import dict2xml

class Crucible(object):
    def __init__(self, baseurl):
        self.baseurl = baseurl

    def get_auth_token(self, username, password):
        request = self.get_auth_token_request(username, password)
        response = self.make_request(request)
        if response.json is None:
            print "An error occurred while trying to get an auth token from crucible"
            return None
        return response.json['token']

    @staticmethod
    def get_auth_token_request(username, password):
        return {
            'method': 'GET',
            'url': '/rest-service/auth-v1/login',
            'params': {
                'userName': username,
                'password': password
            }
        }

    def create_review(self, token, **kwargs):
        request = self.get_create_review_request(token, **kwargs)
        response = self.make_request(request)
        return response

    @staticmethod
    def get_create_review_request(token, **kwargs):
        return {
            'method': 'POST',
            'url': '/rest-service/reviews-v1',
            'params': {
                'FEAUTH': token
            },
            'data': Crucible.get_create_review_payload(**kwargs)
        }

    @staticmethod
    def get_create_review_payload(**kwargs):
        reviewData = {
            'allowReviewersToJoin': kwargs['allow_reviewers_to_join'],
            'author': {'userName': kwargs['author']},
            'creator': {'userName': kwargs['author']},
            'moderator': {'userName': kwargs['author']},
            'description': kwargs['description'],
            'name': kwargs['name'],
            'projectKey': kwargs['project_key']
        }

        return {
            'createReview': {
                'reviewData': reviewData,
                'patch': kwargs['patch']
            }
        }

    @staticmethod
    def prepare_payload(data):
        result = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        result += dict2xml.dict2xml(data)
        return result

    @staticmethod
    def get_headers():
        return {
            'content-type': 'application/xml',
            'accept': 'application/json'
        }

    def make_request(self, request):
        if request['method'] == 'POST':
            return self.make_request_post(request)
        else:
            return self.make_request_get(request)

    def make_request_get(self, request):
        return requests.get(self.combine_url_components(self.baseurl, request['url']),
                            params=request['params'],
                            headers=self.get_headers())

    def make_request_post(self, request):
        return requests.post(self.combine_url_components(self.baseurl, request['url']),
                             params=request['params'],
                             headers=self.get_headers(),
                             data=self.prepare_payload(request['data']))

    @staticmethod
    def combine_url_components(baseurl, therest):
        while baseurl[-1:] == '/':
            baseurl = baseurl[:-1]

        while therest[:1] == '/':
            therest = therest[1:]

        return baseurl + '/' + therest
