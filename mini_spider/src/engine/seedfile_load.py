# -*- coding:utf-8 -*-
#!/usr/bin/env python
"""
读取种子文件，保存队列

Author: maowandong@baidu.com
Date: 2017/04/09 12:30
"""

import logging
import Queue

class SeedFileLoad(object):
    """
    Seed File Load class
    Attributes:
        queue: 种子文件存储队列
    """

    def __init__(self):
        """Inits SeedFileLoad class"""
        self.queue = Queue.Queue()

    def load_seed_file(self, file):
        """
        读取种子文件到队列
        :param file: 种子文件
        :return: 
        """
        try:
            seed_file = open(file, "r")
            for seed in seed_file:
                seed = seed.strip()
                if not seed:
                    self.queue.put(seed)

            seed_file.close()
        except IOError as err:
            logging.error("Read file error: %s" % err)
            return -1


    def get_seed(self):
        return self.queue.get()

    def put_seed(self, item):
        return self.queue.put(item)




