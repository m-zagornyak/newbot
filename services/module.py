from asyncio import coroutine
from importlib import import_module

class Module:
    def __init__(self, ID = None, /, path = None):
        if not ID and not path:
            raise ValueError('Please specify module ID or path')
        if path:
            self.id = '.'.join(path.split('.')[:-1]) \
                                   .replace('\\', '/') \
                                   .replace('../', '') \
                                   .replace('./', '') \
                                   .replace('/', '.')
        else:
            self.id = ID

    def load(self, package = None):
        return import_module(self.id, package)