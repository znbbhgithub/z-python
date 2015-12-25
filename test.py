#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config
import time
import os

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.error('this is test message')
    _LOGGING_CONF_PATH = os.path.abspath(os.path.dirname(__file__)) + '/conf/logging.conf'
    logger.error(_LOGGING_CONF_PATH)
