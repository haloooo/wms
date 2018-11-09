# * coding:utf-8 *
# Author    : Administrator
# Createtime: 11/9/2018
from __future__ import unicode_literals
from django.shortcuts import render
from RtMonSys.models.models_logger import Logger
from django.http import HttpResponse

def go_config(request):
    Logger.write_log("进入basic页面")
    return render(request, 'base/config/index.html')