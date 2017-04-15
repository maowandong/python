# -*- coding:utf-8 -*-
#!/usr/bin/env python
"""
保存已抓取的url

Author: maowandong@baidu.com
Date: 2017/04/10 
"""

import threading

class UrlTable(object):
    """
    处理已爬取url
    Attributes:
        __crawled_url: 存储已爬取的url
    """

    def __init__(self):
        self.__crawled_url = {}
        self.lock = threading.Lock()

    def is_url_crawled(self, url):
        """
        判断url是否已爬取过
        param url: 
        return:
            True: 已爬取
            False: 没有爬取
        """
        self.lock.acquire()
        crawled_url_list = self.__crawled_url.keys()

        if url in crawled_url_list:
            return True
        else:
            return False

        self.lock.release()

    def add_crawled_url(self, url):
        """
        添加已爬取url
        param url: 
        return: 
            
        """
        if not url:
            return True

        self.lock.acquire()
        self.__crawled_url[url] = ''
        self.lock.release()

        return True









