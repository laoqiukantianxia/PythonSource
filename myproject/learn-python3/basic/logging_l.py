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
'''
format: 
asctime: %(asctime)s 日志发生时间戳
levelname: %(levelname)s 日志级别
name: %(name)s 所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
message: %(message)s 日志记录的内容
filename: %(filenames) 文件名(有后缀)
module: %(module)s 文件名(没有后缀)
lineno: %(lineno)s 行号
datefmt
'%m/%d/%Y %I:%M:%S %p' 设置时间格式


format = '%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s - %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')


# use logger
logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)

## create console handle and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

## create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)

## add hander to logger
logger.addHandler(ch)

## log recode:
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
'''

# use logging.conf
import logging.config

logging.config.fileConfig('logging.conf')

## create logger
logger = logging.getLogger('simpleExample')

# log recode
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
