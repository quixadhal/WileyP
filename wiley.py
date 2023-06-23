#!/usr/bin/python3 -B
# -*- coding: utf-8 -*- line endings: unix -*-
__author__ = 'quixadhal'

import os
import sys
import datetime
import logging
import json
# sys.path.append(os.path.join(os.getcwd(), "WileyP"))

# Normally, we always import logging and initialize it BEFORE anything
# else, but in this case, we first need to add to our module search
# path, so we'll trust nothing will explode in os or sys at the top
# level here.

from Mud.log_system import Loggers

log_main = Loggers.addLogger('MAIN')
log_boot = Loggers.addLogger('BOOT')

if __name__ == '__main__':
    log_main.startFileoutput()
    log_main.info('System initializing.')
    start_time = datetime.datetime.utcnow()

    log_boot.startFileoutput()
    log_boot.info('System booting.')
    log_boot.info('Loggers: ' + Loggers.showLoggers())

    log_main.warning('Stuff happens!')
    log_main.stopFileoutput()
    log_main.warning('Sneaky Stuff happens!')
    log_main.startFileoutput()
    log_main.warning('MORE Stuff happens!')
    log_main.stopFileoutput()

    run_length = datetime.datetime.utcnow() - start_time
    log_boot.info('System was up for %s' % run_length)

    log_main.startFileoutput()
    log_boot.critical('System halting.')
    log_boot.stopFileoutput()

    log_main.critical('System halted.')
