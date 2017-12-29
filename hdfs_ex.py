#!/usr/bin/env python3
# coding=utf-8

__author__ = 'chentf'

__version__ = 'v1.0.0'

from hdfs import InsecureClient
from hdfs import Config


def read(client):
    with client.read('/chentf/big', chunk_size=8096) as reader:
        for chunk in reader:
            print(chunk)


def checksum(client, path):
    sum = client.checksum(path)
    print(sum)


def file_continue(client, path, hdfsPath):
    file_status = client._get_file_status(hdfsPath)
    print(type(file_status))
    print(type(file_status.content))
    content = eval(file_status.content)
    already_send = content["FileStatus"]["length"]
    print(already_send)
    file = open(path)
    file.seek(already_send)
    client.write(hdfsPath, file, append=True, buffersize=4096)
    file.close()


if __name__ == '__main__':
    hdfs = "http://xx"
    client = InsecureClient(hdfs, user='hadoop')
    # client = Config().get_client('dev')
    fl = client.list("/chentf");
    print (fl)
    hdfs_path = "/chentf/love2.txt"
    local_path = "d:/love.txt"
    # client.upload(hdfs_path, local_path)
    file_continue(client, local_path, hdfs_path)
    client.download(hdfs_path, "d:/hdfs/" + hdfs_path)
    print("ok")
