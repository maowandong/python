# -*- coding:utf-8 -*-
#!/usr/bin/env python
"""
网页解析处理

Author: maowandong@baidu.com
Date: 2017-04-15 13:30
"""

import logging
import urllib
import urllib2

import chardet

class WebpageParse(object):

    @staticmethod
    def get_html_content(url, timeout=10):
        """
        获取url网页内容
        :param self: 
        :param url: 
        :param timeout: 
        :return: 
        """
        try :
            response = urllib2.urlopen(url, timeout=timeout)
        except urllib2.URLError as err:
            logging.error("url open error: %s" % err)
            return None

        try:
            html_content = response.read()
        except Exception as err:
            logging.error("read http response data error: %s" % err)
            return None

        return WebpageParse.decode_html_content(html_content)

    @staticmethod
    def decode_html_content(html_content):








