#!/usr/bin/env python3
# coding=utf-8
import sys

__author__ = 'chentf'

__version__ = 'v1.0.0'

import pymysql


class makeData(object):
    def __init__(self):
        pass

    def db_conn(self):
        conn = pymysql.connect(host='10.20.107.137', port=3306, user='root', passwd='root', db='sysservice')
        cursor = conn.cursor()
        cursor.execute('SET NAMES UTF8')
        for i in range(100 * 10000):
            self.insert_role(i, cursor)
            if i % 1000 == 0:
                conn.commit()
        conn.commit()
        cursor.close()
        conn.close()

    def insert_role(self, i, cursor):
        sql = """
                insert into t_role(role_id,role_name,role_desp,creation_time,last_modified_time,is_deleted) 
                VALUES (%s,%s,%s,%s,%s,%s)
                 """
        cursor.execute(sql, (
            int(i), "boss" + str(i), "boss" + str(i), "2018-01-18 11:24:49", "2018-01-18 11:24:49", int(0)))

    def insert_user(self, i, cursor):
        sql = """
                insert into t_user(user_password,last_modified_time,creation_time,user_home_url,
                user_real_name,user_phone_number,user_email_address,user_max_resource,
                user_id,is_deleted,customer_id,user_login_name,user_desp) 
                values(%s,now(),now(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                 """
        cursor.execute(sql, (
            '123456', "/root/home/god" + str(i), "god" + str(i), "13858121133", "tfchen5211 @ foxmail.com", "强大的资源"
            , int(i), 0, int(i), "god" + str(i), "god" + str(i)))


if __name__ == '__main__':
    print("hello")
    makeData = makeData()
    makeData.db_conn()
