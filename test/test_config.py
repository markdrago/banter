import unittest
import StringIO

from dejavu.config import Config

class TestConfig(unittest.TestCase):
    def test_get_auth_token(self):
        contents = "[auth]\n"
        contents += "token = mdrago:102:abcdefghijklmnopqrstuvwxyz\n\n"
        c = self.get_config_with_contents(contents)
        expected = "mdrago:102:abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(expected, c.get_value('auth', 'token'))

    def test_get_auth_token_not_present(self):
        contents = "[auth]\n"
        c = self.get_config_with_contents(contents)
        self.assertIsNone(c.get_value('auth', 'token'))

    def test_get_auth_token_no_section(self):
        contents = "[not_auth]\n"
        c = self.get_config_with_contents(contents)
        self.assertIsNone(c.get_value('auth', 'token'))

    def test_set_auth_token(self):
        #setup a primed config object
        contents = "[auth]\n"
        contents += "token = mdrago:102:abcdefghijklmnopqrstuvwxyz\n\n"
        c = self.get_config_with_contents(contents)

        #create a stringIO object to receive the changes and set the new token
        fp = StringIO.StringIO()
        newtoken = "mdrago:104:wheredidthealphabetgo"
        c.set_value('auth', 'token', newtoken, fp=fp)
        filecontents = fp.getvalue()
        fp.close()

        #verify that the new token was written
        expected = "[auth]\n"
        expected += "token = mdrago:104:wheredidthealphabetgo\n\n"
        self.assertEqual(expected, filecontents)

    @staticmethod
    def get_config_with_contents(contents):
        buffer = StringIO.StringIO(contents)
        c = Config()
        c.load_from_file_pointer(buffer)
        buffer.close()
        return c
