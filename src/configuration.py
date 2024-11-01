import json

'''
Usage:
conf = Config.load_json('config.json') v# Configuration isn't instantiated, the methods are static

returns a Dict, which is different to dict, in that you can use .notation 

Data (attributes) are accessed through dot . notation 
conf.version
conf.file_path
conf.dark_mode
etc.
'''


# Code from https://stackoverflow.com/a/68244012/19674377 
class Dict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

class Config(object):
    @staticmethod
    def __load__(data):
        if type(data) is dict:
            return Config.load_dict(data)
        elif type(data) is list:
            return Config.load_list(data)
        else:
            return data

    @staticmethod
    def load_dict(data: dict):
        result = Dict()
        for key, value in data.items():
            result[key] = Config.__load__(value)
        return result

    @staticmethod
    def load_list(data: list):
        result = [Config.__load__(item) for item in data]
        return result

    @staticmethod
    def load_json(path: str):
        with open(path, "r") as f:
            result = Config.__load__(json.loads(f.read()))
        return result
    
    @staticmethod
    def save_json(data: Dict, path: str): 
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def __repr__(self):
        return "Config object: {}".format(self.__dict__["version"])
    
