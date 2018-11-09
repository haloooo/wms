# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

# Create your models here.

class Logger(object):
    @staticmethod
    def write_log(msg):
        try:
            logger = logging.getLogger("info")
            logger.info(msg)
        except BaseException as exp:
            logger = logging.getLogger("django.request")
            logger.error(exp.message)

    @staticmethod
    def file_log(desc, filepath):
        try:
            logger = logging.getLogger("file")
            logger.info(desc + ": " + filepath)
        except BaseException as exp:
            logger = logging.getLogger("django.request")
            logger.error(desc + ": " + exp.message)





