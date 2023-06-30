# -*- coding: utf-8 -*- line endings: unix -*-
__author__ = 'quixadhal'

from Mud.log_system import Loggers

log_main = Loggers.addLogger('MAIN')

def test_func():
    log_main.info("This is just a test")
