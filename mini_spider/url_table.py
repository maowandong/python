# -*- coding:utf-8 -*-
#!/usr/bin/env python
"""
保存已抓取的url

Author: maowandong@baidu.com
Date: 2017/04/10 
"""

import threading
import Queue



LOCK = threading.Lock()
URL_QUEUE = Queue.Queue()
CRAWLED_URLS = set()