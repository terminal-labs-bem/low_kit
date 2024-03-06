import os
import inspect
import importlib.metadata
from pathlib import Path
from lowkit.settings import VERSION, PROJECT_NAME, PROJECT_ROOT

def info():
    return {"PROJECT_ROOT":PROJECT_ROOT, "PROJECT_NAME":PROJECT_NAME, "VERSION":VERSION}

def call_order():
    stack = inspect.stack()
    calls = []
    for s in reversed(stack):
        calls.append(s.filename)
    return calls

def caller_info():
    def _get_call_order(stack):
        counter = 0
        for s in reversed(stack):
            counter = counter + 1
            if ".py" in s.filename:
                return counter
        return 0

    stack = inspect.stack()
    parentframe = stack[len(stack) - _get_call_order(stack)][0]

    module_info = inspect.getmodule(parentframe)
    if module_info:
        mod = module_info.__name__.split('.')
        package = mod[0]
        module = mod[1]

    klass = None
    if 'self' in parentframe.f_locals:
        klass = parentframe.f_locals['self'].__class__.__name__

    caller = None
    if parentframe.f_code.co_name != '<module>':
        caller = parentframe.f_code.co_name

    line = parentframe.f_lineno

    return package, module, klass, caller, line

def get_distribution_name():
    package, module, klass, caller, line = caller_info()
    name = package
    return name

def get_distribution_source():
    calls = call_order()
    for call in calls:
        if ".py" in call:
            path = Path(call)
            return path.parent.absolute()

def get_distribution_files(name):
    files = []
    for f in importlib.metadata.files(name):
        path = str(f.locate())
        path = os.path.basename(path)
        files.append(path)
    return files

def get_distribution_filepaths(name):
    files = []
    for f in importlib.metadata.files(name):
        path = str(f.locate())
        files.append(path)
    return files

def get_distribution_version(name):
    version = importlib.metadata.version(name)
    return version

def get_distribution_asset_filepath_by_ext(ext):
    path = get_distribution_source()
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.' + ext in file:
                files.append(os.path.join(r, file))
    return files

def distribution_install_editable(name):
    for f in importlib.metadata.files(name):
        path = str(f.locate())
        if 'site-packages' in path and '.pth' in path:
            return True
        else:
            return False
