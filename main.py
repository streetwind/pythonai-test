#!/usr/bin/env python
# -*- coding: utf-8 -*-

from module.config import windconfig as config
import logging as log


class Wind(object):
    def __init__(self):
        config.init()
        log.debug('错误日志')
        print(config.get("baiduapi"))
        pass

if __name__ == "__main__":
    windsystem= Wind()
