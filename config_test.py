#!/usr/bin/env python3
# coding=utf-8

import ConfigParser

if __name__ == '__main__':
    cf = ConfigParser.ConfigParser()
    cf.read("config.ini")
    secs = cf.sections()
    print(secs)
    items = cf.items("sec_b")
    print(cf.get("hdfs", "hdfs_url"))
