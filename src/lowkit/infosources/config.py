import os
import sys
import time
import json

import configparser

def getconfig():
    config_object = configparser.ConfigParser()
    file = open("config.ini","r")
    config_object.read_file(file)
    output_dict=dict()
    sections=config_object.sections()
    for section in sections:
        items=config_object.items(section)
        output_dict[section]=dict(items)
    return output_dict


def find_config(packagename):
	return os.listdir(os.path.abspath(os.getcwd()))
	# if in cwd
	# if in search plugins
	#else use default -- merge in defaults

def extend_config():
	pass
	## add config class
	## add config type
	## add config source
