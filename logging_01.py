#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config

if __name__ == '__main__':
    logging.config.fileConfig('config.ini')
    logger = logging.getLogger(__name__)

    logger.debug('this is debug message')
    logger.info('this is info message')
    logger.warning('this is warning message')
    logger.error('this is error message')
    logger.critical('this is critical message')
