#!/usr/bin/env python3
# coding=utf-8

__author__ = 'chentf'

__version__ = 'v1.0.0'

import etcd


def set_val(etcd_client, local_file_path, etcd_path):
    input = open(local_file_path)
    content = input.read()
    etcd_client.set(etcd_path, content)


if __name__ == '__main__':
    etcd_location = ["172.32.1.61", 4001]
    # etcd_location = ["172.32.1.58", 2379]
    etcd_client = etcd.Client(host=etcd_location[0], port=etcd_location[1])
    # set_val(etcd_client, "d:/config_env.json", "/test/abc")
    print(etcd_client.get("/llbrain/apps/euler-chentf/config/rpcservice/euler"))
