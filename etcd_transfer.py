#!/usr/bin/env python3
# coding=utf-8

__author__ = 'chentf'

__version__ = 'v1.0.0'

import etcd


def transfer(resource_ip, resource_root, target_ip, target_root):
    resource_client = etcd.Client(host=resource_ip[0], port=resource_ip[1])
    target_client = etcd.Client(host=target_ip[0], port=target_ip[1])
    # target_client.delete('/test', recursive=True)
    doit(resource_client, resource_root, target_client, target_root)
    pass


def doit(resource_client, key, target_client, root_key):
    etcd_result = resource_client.get(key)
    # If it's a folder
    if (key == None or key == "/"):
        key = root_key
    else:
        key = root_key + key

    if etcd_result.dir == True:
        # The new folder
        # etcd_result.ttl = 60
        if (key == None or key == "/"):
            pass
        else:
            target_client.write(key=key, value=None, dir=True, ttl=etcd_result.ttl)
        #  Traverse the child nodes
        for i in etcd_result._children:
            doit(resource_client, i.get("key"), target_client, root_key)
    else:
        # etcd_result.ttl = 60
        target_client.write(key=key, value=etcd_result.value, dir=False, ttl=etcd_result.ttl)
        print("write-key[%s]-value[%s]", key, etcd_result.value)


if __name__ == '__main__':
    resource_ip = ["172.32.1.58", 2379]
    resource_root = "/"
    target_ip = ["172.26.12.61", 4001]
    target_root = "/"
    transfer(resource_ip, resource_root, target_ip, target_root)
