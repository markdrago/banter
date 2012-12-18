import sys
import os
import ConfigParser

class Config(object):
    def __init__(self):
        self.parser = ConfigParser.SafeConfigParser()
        self.filename = os.path.expanduser('~/.config/banter/banter.conf')

    def load_from_file(self):
        self.parser.read(self.filename)

    def load_from_file_pointer(self, fp):
        self.parser.readfp(fp)

    def as_dict(self):
        main_dict = {}
        for section in self.parser.sections():
            main_dict[section] = dict(self.parser.items(section))
        return main_dict

    def set_from_dict(self, new_dict):
        for section in new_dict.keys():
            for keyname in new_dict[section]:
                self.set_value(section, keyname, new_dict[section][keyname])

    def get_value(self, section, key):
        try:
            return self.parser.get(section, key)
        except ConfigParser.Error as e:
            return None

    def set_value(self, section, key, value):
        if not self.parser.has_section(section):
            self.parser.add_section(section)
        self.parser.set(section, key, value)

    def save(self):
        fp = self.open_config_file_for_writing()
        self.save_fp(fp)
        fp.close()

    def save_fp(self, fp):
        self.parser.write(fp)

    def open_config_file_for_writing(self):
        dirname = os.path.dirname(self.filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        return open(self.filename, "w")
