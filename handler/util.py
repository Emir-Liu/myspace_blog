import configparser
import os

class ReadConfig():
    def __init__(self):
        self.BASE_DIRS = os.path.dirname(__file__)
        config_path = 'config/config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get(self,section,key):
        return self.config.get(section,key)
