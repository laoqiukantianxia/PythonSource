# -*- coding:utf-8 -*-

mode = 2

if mode == 0:
    """
    基本用法：
    """
    import logging
    logging.info('test')  # 默认的打印级别是warning，此处不会打印
    logging.warn('test')
elif mode == 1:
    """
    basicConfig配置：
    1. level：打印级别
    2. filename：输出文件
    3. format：打印格式
        * asctime: %(asctime)s 日志发生时间戳
        * levelname: %(levelname)s 日志级别
        * name: %(name)s 所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
        * message: %(message)s 日志记录的内容
        * filename: %(filenames) 文件名(有后缀)
        * module: %(module)s 文件名(没有后缀)
        * lineno: %(lineno)s 行号
    4. datefmt：时间格式，'%Y-%m-%d %H:%M:%S'
        
    """
    import logging
    import time
    format = '%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename='example.log', format=format, level=logging.DEBUG)
    logging.info('%s', time.strftime('%Y-%m-%d %H:%M:%S'))
elif mode == 2:
    '''
    logging高级用法：
    1. 四大组件：
        记录器    Logger    提供了应用程序可一直使用的接口
        处理器    Handler   将logger创建的日志记录发送到合适的目的输出
        过滤器    Filter    提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
        格式器    Formatter 决定日志记录的最终输出格式
    
    即：日志器（logger）是入口，真正干活儿的是处理器（handler），
    （handler）还可以通过过滤器（filter）和格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作。
    '''
    import logging
    import time
    # a. 初始化logger,设置日志级别
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # b. 初始化处理器，格式器
    #   * FileHandler，文件；
    #   * StreamHandler，标准输入输出，默认sys.stderr
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler('example.log', encoding='utf8')
    ch = logging.StreamHandler()
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    # 日志记录
    logger.info('%s', '记录器使用')
elif mode == 3:
    """
    配置文件使用
    """
    pass
