# -*- coding:utf-8 -*-

import logging

'''
# simple
logging.warning('task')
logging.info('task') # 默认级别是warning，此处不会打印

# output file
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

# recv command line argument
loglevel = 'debug'
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)
print('log level: ', numeric_level)
'''

# change output format
format = '%(levelname)s - %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')
