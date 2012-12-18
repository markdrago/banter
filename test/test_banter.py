import unittest

from banter import banter

class TestBanter(unittest.TestCase):
    def setUp(self):
        self.c = MockConfig()
        self.c.set_value('crucible', 'url', 'http://host/fisheye')
        self.c.set_value('crucible', 'username', 'mdrago')
        self.c.set_value('crucible', 'token', 'blahblah')
        self.c.set_value('crucible', 'project_key', 'CR')

    def test_required_fields_all_present(self):
        self.assertTrue(banter.has_all_required_fields(self.c))

    def test_required_fields_url_missing(self):
        self.c.remove_value('crucible', 'url')
        self.assertFalse(banter.has_all_required_fields(self.c))

    def test_required_fields_username_missing(self):
        self.c.remove_value('crucible', 'username')
        self.assertFalse(banter.has_all_required_fields(self.c))

    def test_required_fields_token_missing(self):
        self.c.remove_value('crucible', 'token')
        self.assertFalse(banter.has_all_required_fields(self.c))

    def test_required_fields_project_key_missing(self):
        self.c.remove_value('crucible', 'project_key')
        self.assertFalse(banter.has_all_required_fields(self.c))

class MockConfig(object):
    def __init__(self):
        self.sections = {}

    def set_value(self, section, name, value):
        if section not in self.sections:
            self.sections[section] = {}
        self.sections[section][name] = value

    def remove_value(self, section, name):
        if section in self.sections and name in self.sections[section]:
            del self.sections[section][name]

    def get_value(self, section, name):
        if section not in self.sections or name not in self.sections[section]:
            return None
        return self.sections[section][name]
