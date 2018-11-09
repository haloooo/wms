# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.db import connections
import os
import re

def get_config(key):
    # 加载配置文件
    file_path = os.getcwd() + '/config/config.json'
    fp = open(file_path)
    json_data = json.load(fp)
    return json_data[key]

