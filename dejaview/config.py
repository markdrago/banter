import sys
import os
import ConfigParser

class Config(object):
    def __init__(self):
        self.parser = ConfigParser.SafeConfigParser()
        self.filename = os.path.expanduser('~/.config/dejaview/dejaview.conf')

    def load_from_file(self):
        self.parser.read(self.filename)

    def load_from_file_pointer(self, fp):
        self.parser.readfp(fp)

    def get_value(self, section, key):
        try:
            return self.parser.get(section, key)
        except ConfigParser.Error as e:
            return None

    def set_value(self, section, key, value, fp=None):
        should_close_fp = False
        if fp is None:
            should_close_fp = True
            fp = self.open_config_file_for_writing()

        if not self.parser.has_section(section):
            self.parser.add_section(section)

        self.parser.set(section, key, value)

        self.parser.write(fp)
        if should_close_fp:
            fp.close()

    def open_config_file_for_writing(self):
        dirname = os.path.dirname(self.filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        return open(self.filename, "w")
