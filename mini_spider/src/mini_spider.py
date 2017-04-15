# -*- coding:utf-8 -*-
#!/usr/bin/env python
"""
mini_spider主程序

Author: maowandong@baidu.com
Date: 2017/04/10 10:05
"""

import argparse

import config_load
import log

version = "1.0.0"

def arg_parse():
    """
    命令行参数解析
    Returns: 
        configure file name
    """
    description = "mini spider"
    parser = argparse.ArgumentParser(description=description)
    version_info = "mini spirder %s" % version
    parser.add_argument('-v', help='version of mini spider', action='version', version=version_info)
    parser.add_argument('-c','--config', help='configure file', required=True)
    options = parser.parse_args()

    return options.config

def main():
    """
    主程序入口
    """

    # 初始化log
    log.init_log("./log/spider")
    #解析命令行参数，获取配置文件信息
    conf_name = arg_parse()
    config_load.parse_conf(conf_name)

if __name__ == '__main__':
    main()


