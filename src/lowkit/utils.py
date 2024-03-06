import os
import sys
import copy
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
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import os
import binascii
import pickle
import glob

from tempfile import mkstemp
from shutil import move
from os import remove

weekdays = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
hours = [
    (0, "12am"),
    (1, "1am"),
    (2, "2am"),
    (3, "3am"),
    (4, "4am"),
    (5, "5am"),
    (6, "6am"),
    (7, "7am"),
    (8, "8am"),
    (9, "9am"),
    (10, "10am"),
    (11, "11am"),
    (12, "12pm"),
    (13, "1pm"),
    (14, "2pm"),
    (15, "3pm"),
    (16, "4pm"),
    (17, "5pm"),
    (18, "6pm"),
    (19, "7pm"),
    (20, "8pm"),
    (21, "9pm"),
    (22, "10pm"),
    (23, "11pm"),
]

runtimes = []

for weekday in weekdays:
    for hour in hours:
        runtimes.append((weekday, hour[1]))

excluded_dirs = [".DS_Store"]


def stdio_print(data):
    if PRINT_VERBOSITY == "high":
        print(data)


def read_file(fname):
    with open(fname, "rb") as f:
        content = f.read()
    return content


def write_file(data, path):
    with open(path, "wb") as the_file:
        the_file.write(data)


def bytes_to_hex_str(data):
    data = pickle.dumps(data)
    data = binascii.b2a_hex(data)
    data = data.decode("utf-8")
    return data


def hex_str_to_bytes(data):
    data = binascii.a2b_hex(data)
    data = pickle.loads(data)
    return data


def empty_dir(path):
    files = glob.glob(path + "/*")
    for f in files:
        if os.path.isfile(f):
            os.remove(f)


def ping(host):
    res = False

    ping_param = "-c 1"

    resultado = os.popen("ping " + ping_param + " " + host).read()

    if "ttl=" in resultado:
        res = True
    return res

def _delete_dir(directory):
    directory = abspath(directory)
    if exists(directory):
        shutil.rmtree(directory)

def _copy_dir(source, target):
    if not exists(target):
        shutil.copytree(abspath(source), abspath(target))

def _rename_dir(source, target):
    os.rename(source, target)

def _fast_scandir_shallow(dirname):
    subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
    return subfolders

def _fast_scandir(dirname):
    subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(_fast_scandir(dirname))
    return subfolders


def _fast_scandfiles(dirname):
    dirs = _fast_scandir(dirname)
    files = [f.path for f in os.scandir(dirname) if f.is_file()]
    for dir in dirs:
        files.extend([f.path for f in os.scandir(dir) if f.is_file()])
    return files

def _replace(source_file_path, pattern, substring):
    fh, target_file_path = mkstemp()
    with open(target_file_path, 'w') as target_file:
        with open(source_file_path, 'r') as source_file:
            for line in source_file:
                target_file.write(line.replace(pattern, substring))
    remove(source_file_path)
    move(target_file_path, source_file_path)

def match_ignore_whitespace(a, b):
    if a.strip() == b.strip(): 
        return True
    else:
        return False

def _replace_many_lines(source_file_path, patterns):
    with open(source_file_path) as f:
        lines = [line for line in f]

    for line in lines:
        for pattern in patterns:
            if match_ignore_whitespace(line, pattern[0]):
                lines[lines.index(line)] = pattern[1] + "\n"


    fh, target_file_path = mkstemp()
    with open(target_file_path, 'w') as target_file:
        for line in lines:
            target_file.write(line)
    remove(source_file_path)
    move(target_file_path, source_file_path)
