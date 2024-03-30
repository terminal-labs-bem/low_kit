import os
import sys
from os import listdir
from os.path import isfile, join
import importlib
import importlib.util
import os
import shutil
import urllib
import subprocess
from urllib.request import urlopen
from os.path import isdir, dirname, realpath, abspath, join, exists
from zipfile import ZipFile
from configparser import ConfigParser

def dl_zip(url, name, workingdir):
    if not exists(workingdir + name):
        with urlopen(url) as response, open(workingdir + name, "wb") as out_file:
            shutil.copyfileobj(response, out_file)


def unzip(source, extract):
    with ZipFile(source) as zf:
        zf.extractall(path=extract)
