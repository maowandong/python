# -*- coding:utf-8 -*-
#!/usr/bin/env python
"""
将网页保存到磁盘
"""

import os


class SaveWebPage(object):
    """
    保存解析的网页内容到本地磁盘
    Attributes:
        output_dir: 保存解析的网页内容       
    """

    def __init__(self, output_dir):
        """解析后保存的目录"""
        self.output_dir = output_dir

    def save_content(self):
        pass
