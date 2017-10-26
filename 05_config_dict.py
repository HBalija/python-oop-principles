#!/usr/bin/python3

import json
import os


class ConfigKeyError(Exception):

    def __init__(self, key, dic):

        self.key = key
        self.keys = dic.keys()

    def __str__(self):
        return 'Key "{0}" not found. Existing keys: {1}'.format(
            self.key, ', '.join(self.keys))


class ConfigDict(dict):

    def __init__(self, filename):

        self.filename = filename
        if not os.path.isfile(self.filename):
            try:
                # trying to create an empty json file and store a dict in it.
                with open(self.filename, 'w') as fh:
                    json.dump({}, fh)
            except IOError:
                # raising error if bad path
                raise IOError('Not a valid pathname: {}'.format(self.filename))

        with open(self.filename) as fh:
            conf = json.load(fh)
            # displaying content of config file with print
            self.update(conf)

    def __getitem__(self, key):

        if key not in self:
            raise ConfigKeyError(key, self)
        return super().__getitem__(key)

    def __setitem__(self, key, val):

        super().__setitem__(key, val)
        with open(self.filename, 'w') as fh:
            json.dump(self, fh)

    def load_file(self):
        for key in self:
            os.environ[key] = self[key]

# example

config_dict = ConfigDict('config.json')
config_dict['DEBUG'] = False

print(d)
