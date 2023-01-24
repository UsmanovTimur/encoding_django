import sys
import base64
from importlib import invalidate_caches
from importlib.abc import SourceLoader
from importlib.machinery import FileFinder


class MyFinder(FileFinder):
    PATH_TRIGGER = '/code/'

    def __init__(self, path_entry: str, *loader_details):
        if path_entry.find(self.PATH_TRIGGER) == -1:
            raise ImportError()
        super(MyFinder, self).__init__(path_entry, *loader_details)


class MyLoader(SourceLoader):
    def __init__(self, fullname, path):
        self.fullname = fullname
        self.path = path

    def get_filename(self, fullname):
        return self.path

    def get_data(self, filename):
        with open(filename) as f:
            a = f.read().encode('utf-8')
            if a == b"":
                return a
            data = base64.b64decode(a)
        return data


loader_details = MyLoader, [".py"]


def install():
    sys.path_hooks.insert(0, MyFinder.path_hook(loader_details))
    sys.path_importer_cache.clear()
    invalidate_caches()
