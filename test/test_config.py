import unittest
from mock import Mock
import StringIO

from banter import config

class TestConfig(unittest.TestCase):
    def test_get_value(self):
        contents = "[auth]\n"
        contents += "token = mdrago:102:abcdefghijklmnopqrstuvwxyz\n\n"
        c = self.get_config_with_contents(contents)
        expected = "mdrago:102:abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(expected, c.get_value('auth', 'token'))

    def test_get_value_when_value_not_present(self):
        contents = "[auth]\n"
        c = self.get_config_with_contents(contents)
        self.assertIsNone(c.get_value('auth', 'token'))

    def test_get_value_when_section_not_present(self):
        contents = "[not_auth]\n"
        c = self.get_config_with_contents(contents)
        self.assertIsNone(c.get_value('auth', 'token'))

    def test_set_value_and_save_overwrites_existing_value(self):
        #setup a primed config object
        contents = "[auth]\n"
        contents += "token = mdrago:102:abcdefghijklmnopqrstuvwxyz\n\n"
        c = self.get_config_with_contents(contents)

        #create a stringIO object to receive the changes and set the new token
        newtoken = "mdrago:104:wheredidthealphabetgo"
        c.set_value('auth', 'token', newtoken)

        fp = StringIO.StringIO()
        c.save_fp(fp)
        filecontents = fp.getvalue()
        fp.close()

        #verify that the new token was written
        expected = "[auth]\n"
        expected += "token = mdrago:104:wheredidthealphabetgo\n\n"
        self.assertEqual(expected, filecontents)

    @staticmethod
    def get_config_with_contents(contents):
        buffer = StringIO.StringIO(contents)
        c = config.Config()
        c.load_from_file_pointer(buffer)
        buffer.close()
        return c

    def test_load_from_file_calls_config_parser_read(self):
        c = config.Config()
        c.parser = Mock()
        c.filename = '/tmp/configfile'
        c.load_from_file()
        c.parser.read.assert_called_with('/tmp/configfile')

    def test_as_dict(self):
        c = config.Config()
        c.set_value('sec1', 'key1', 'val1')
        c.set_value('sec1', 'key2', 'val2')
        c.set_value('sec2', 'key3', 'val3')
        expected = {
            'sec1': {
                'key1': 'val1',
                'key2': 'val2'
            },
            'sec2': {
                'key3': 'val3'
            }
        }
        self.assertEqual(expected, c.as_dict())

    def set_from_dict(self):
        c = config.Config()
        replacement = {
            'sec1': {
                'key1': 'val1',
                'key2': 'val2'
            },
            'sec2': {
                'key3': 'val3'
            }
        }
        c.set_from_dict(replacement)
        self.assertEqual('val1', c.get_value('sec1', 'key1'))
        self.assertEqual('val2', c.get_value('sec1', 'key2'))
        self.assertEqual('val3', c.get_value('sec2', 'key3'))
