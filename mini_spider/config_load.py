# -*- coding:utf-8 -*-
#!/usr/bin/env python
"""
读取配置文件

Author: maowandong
Date: 2017/04/10 11:12
"""

import ConfigParser
import logging
import os

URL_LIST_FILE=''
OUTPUT_DIRECTORY=''
MAX_DEPTH=''
CRAWL_INTERVAL=0
CRAWL_TIMEOUT=0
TARGET_URL=''
THREAD_COUNT=0

def parse_conf(conf_file):
    """
    解析配置文件，将对应的spider配置信息存储在url_table中    
    :param conf_file: 
    :return: 
        0 解析成功
        -1 解析失败
    """
    if not os.path.exists(conf_file):
        logging.error("Config file %s do not exist!" % conf_file)
        return -1

    config = ConfigParser.ConfigParser()
    config.read(conf_file)
    try:
        URL_LIST_FILE = config.get('spider', 'url_list_file')
        OUTPUT_DIRECTORY = config.get('spider', 'output_directory')
        MAX_DEPTH = config.get('spider', 'max_depth')
        CRAWL_INTERVAL = config.get('spider', 'crawl_interval')
        CRAWL_TIMEOUT = config.get('spider', 'crawl_timeout')
        TARGET_URL  = config.get('spider', 'target_url')
        THREAD_COUNT = config.get('spider', 'thread_count')

        logging.info("Read global values from %s successfully" % conf_file)
        return 0
    except ValueError as err:
        logging.error("Read global value error, error message: %s ", err)
        return -1