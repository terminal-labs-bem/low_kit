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

from tempfile import mkstemp
from shutil import move
from os import remove


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
