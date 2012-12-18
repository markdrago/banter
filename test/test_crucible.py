import unittest

from banter import crucible

class TestRequest(unittest.TestCase):
    def setUp(self):
        self.c = crucible.Crucible('http://base/dir')

    def test_get_auth_token_request(self):
        r = self.c.get_auth_token_request('myuser', 'mypass')
        self.assertEqual('GET', r['method'])
        self.assertEqual('/rest-service/auth-v1/login', r['url'])
        self.assertEqual('myuser', r['params']['userName'])
        self.assertEqual('mypass', r['params']['password'])

    def test_get_create_review_request(self):
        r = self.c.get_create_review_request(
            'usertoken',
            **self.sample_create_review_params()
        )
        self.assertEqual('POST', r['method'])
        self.assertEqual('/rest-service/reviews-v1', r['url'])
        self.assertEqual('usertoken', r['params']['FEAUTH'])
        self.assertIsNotNone(r['data'])

    def test_get_create_review_payload(self):
        payload = self.c.get_create_review_payload(
            **self.sample_create_review_params()
        )
        review_data = payload['createReview']['reviewData']
        self.assertEqual(True, review_data['allowReviewersToJoin'])
        self.assertEqual('mdrago', review_data['author']['userName'])
        self.assertEqual('mdrago', review_data['creator']['userName'])
        self.assertEqual('description here', review_data['description'])
        self.assertEqual('name here', review_data['name'])
        self.assertEqual('CR', review_data['projectKey'])
        self.assertEqual('<![CDATA[patch here]]>', payload['createReview']['patch'])

    def test_prepare_xml_payload(self):
        r = {
            'createReview': {
                'reviewData': {
                    'allowReviewersToJoin': True
                }
            }
        }
        expected = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        expected += '<createReview>'
        expected += '<reviewData>'
        expected += '<allowReviewersToJoin>true</allowReviewersToJoin>'
        expected += '</reviewData>'
        expected += '</createReview>'
        self.assertEqual(expected, self.c.prepare_xml_payload(r))

    @staticmethod
    def sample_create_review_params():
        return {
            'allow_reviewers_to_join': True,
            'author': 'mdrago',
            'description': 'description here',
            'name': 'name here',
            'project_key': 'CR',
            'patch': "patch here"
        }
