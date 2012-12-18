import unittest

from banter import utils

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.host = "http://hostname.com"

    def test_combine_url_components_simple(self):
        result = utils.combine_url_components(self.host, "directory")
        self.assertEqual(self.host + "/directory", result)

    def test_combine_url_components_multiple(self):
        result = utils.combine_url_components(self.host, "dir", "file")
        self.assertEqual(self.host + "/dir/file", result)

    def test_combine_url_components_messy(self):
        result = utils.combine_url_components(self.host + '/', "//dir/", "/file//")
        self.assertEqual(self.host + "/dir/file", result)
