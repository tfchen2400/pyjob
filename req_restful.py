#!/usr/bin/env python3
# coding=utf-8
"""
    restful
"""
import urllib.request
import time


class ReqRestful(object):
    def __init__(self):
        pass

    def do_request(self):
        req = urllib.request.urlopen(self.url)
        str = req.read().decode('utf-8')
        print(str)
        return str


if __name__ == '__main__':
    req = ReqRestful()

    for i in range(100000):
        time.sleep(0.2)
        print(i)
        req.url = 'http://127.0.0.1:8051/client/center/chentf/put?document=' + str(i)
        req.do_request()
