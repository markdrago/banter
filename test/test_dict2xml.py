import unittest

from dejavu import dict2xml

class TestDict2Xml(unittest.TestCase):
    def test_single_tag(self):
        d = {'a': 1}
        expected = '<a>1</a>'
        self.assertEqual(expected, dict2xml.dict2xml(d))

    def test_single_boolean_tag(self):
        d = {'a': True}
        expected = '<a>true</a>'
        self.assertEqual(expected, dict2xml.dict2xml(d))

    def test_multiple_tags(self):
        d = {'a': 1,
             'b': 'two'}
        expected = "<a>1</a>"
        expected += "<b>two</b>"
        self.assertEqual(expected, dict2xml.dict2xml(d))

    def test_multiple_tags_pretty(self):
        d = {'a': 1,
             'b': 'two'}
        expected = "<a>1</a>"
        expected += "\n<b>two</b>"
        self.assertEqual(expected, dict2xml.dict2xml(d, pretty=True))

    def test_nested_tags(self):
        d = {
            'outer': {
                'inner': 'tag'
            }
        }
        expected = "<outer><inner>tag</inner></outer>"
        self.assertEqual(expected, dict2xml.dict2xml(d))

    def test_nested_tags_pretty(self):
        d = {
            'outer': {
                'inner': 'tag'
            }
        }
        expected = "<outer>\n"
        expected += "    <inner>tag</inner>\n"
        expected += "</outer>"
        self.assertEqual(expected, dict2xml.dict2xml(d, pretty=True))

    def test_nested_tags_multiple_kids_pretty(self):
        d = {
            'outer': {
                'inner': 'tag',
                'inner2': 'tag2'
            }
        }
        expected = "<outer>\n"
        expected += "    <inner2>tag2</inner2>\n"
        expected += "    <inner>tag</inner>\n"
        expected += "</outer>"
        self.assertEqual(expected, dict2xml.dict2xml(d, pretty=True))
