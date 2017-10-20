#!/usr/bin/env python3
# coding=utf-8

__author__ = 'chentf'

__version__ = 'v1.0.0'

import urllib
from urllib import parse
from flask import json
import pymysql


class ReqRestful(object):
    def __init__(self):
        pass

    def do_request(self):
        test_data_urlencode = parse.urlencode(self.data)
        req = urllib.request.urlopen(self.url + "?" + test_data_urlencode)
        str = req.read().decode('utf-8')
        self.res = str
        # print(str)
        return str

    def analysis(self):
        rjson = json.loads(self.res)
        rlist = []
        for k, v in rjson["paths"].items():
            for m, o in v.items():
                temp = {}
                temp['path'] = k
                temp['method'] = m
                temp['memo'] = str(o['tags']) + o['summary']
                rlist.append(temp)
                print(m)
        self.rlist = rlist
        for i in rlist:
            print(i)
        return rlist

    def db_conn(self):
        conn = pymysql.connect(host='192.168.59.164', port=3306, user='root', passwd='123456', db='qh_usercenter')
        cursor = conn.cursor()
        cursor.execute('SET NAMES UTF8')
        for i in self.rlist:
            str = "insert into qh_menu_restful(menu_id,restful_url,type,memo) VALUES (0,'" + i["path"] + "','" + i[
                "method"].upper() + "','" + i["memo"].replace("'", "") + "')"
            str = str.encode("utf-8")
            print(str)
            try:
                effect_row = cursor.execute(str)
            except Exception  as e:
                print(e)

        conn.commit()
        cursor.close()
        conn.close()
        print(effect_row)

    def insert_db(self):
        self.db_conn()
        for r in self.rlist:
            print(r)


if __name__ == '__main__':
    req = ReqRestful()
    req.data = ""
    req.url = 'http://192.168.59.236:8082/console/v2/api-docs'
    req.do_request()
    req.analysis()
    req.insert_db()
    print("hello")