# -*- coding:utf-8 -*-
#!/usr/bin/env python

"""
抓取线程

Author: maowandong@baidu.com
Date: 2017-04-15 11:30
"""

import threading
import urllib
import urllib2

class CrawlThread(threading.Thread):
    """
    多线程爬取处理类
    
    Attributes:
        queue: 种子文件存储队列
    """

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        pass

