from os.path import dirname, basename, isfile
from glob import glob

_dir = dirname(__file__) + r"\*.py"
modules = glob(_dir)
for module in modules:
    if isfile(module) and not module.endswith("__init__.py"):
        __all__ = basename(module)[:-3]