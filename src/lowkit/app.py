import os
import sys
import time
import json
import yaml
import shutil
import hashlib
import zipfile
import base64
import uuid
from os import environ
from pathlib import Path

import requests
import click
from flask import Flask, jsonify, request

from cli_passthrough import cli_passthrough

from basekit.objects import globalconfig
from basekit.ops.scaffolding import set_global_bracket_data, get_global_bracket_data
from basekit.ops.scaffolding import get_hydrated_scaffolding_paths, build_scaffolding, test_scaffolding, get_scaffolding_style, scaffolding_styles
from basekit.infosources.distribution import get_distribution_name, get_distribution_version, distribution_install_editable, caller_info, call_order, get_distribution_files, get_distribution_filepaths

def main():
    print(scaffolding_styles)
    set_global_bracket_data("/home/user/Desktop/bench/bridge_pilot", "/home/user", "bridgepilot")
    #get_global_bracket_data()
    build_scaffolding("workstation")
    # test_scaffolding_style()
    # print(get_scaffolding_style())
    # name = get_distribution_name()
    # print(name)
    # print(get_distribution_version(name))
    # print(distribution_install_editable(name))
    # print(call_order())
    # print(get_distribution_files(name))
    # print(get_distribution_filepaths(name))
    # print(get_distribution_src_path(name))
    # print(get_distribution_pth_path(name))
    # print(get_distribution_pth_content(name))

def start_main():
   	main()