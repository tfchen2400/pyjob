#!/usr/bin/env python3
# coding=utf-8
import os

__author__ = 'chentf'

__version__ = 'v1.0.0'

from hdfs import InsecureClient
import ConfigParser


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
    cf = ConfigParser.ConfigParser()
    cf.read("config.ini")

    hdfs = cf.get("hdfs", "hdfs_url")
    client = InsecureClient(hdfs, user='hadoop')
    # client = Config().get_client('dev')
    fl = client.list("/launcher/task_file/264805379706191872")
    # client.makedirs("/launcher/code/")
    print (fl)
    hdfs_path = "/launcher/task_file/264805379706191872/264805379706191872.zip"
    local_path = "d:/hdfs/" + hdfs_path
    localinfo = os.path.split(local_path)
    localdir = localinfo[0]
    if os.path.exists(localdir) == False:
        os.makedirs(localdir)
    # client.download(hdfs_path, "d:/hdfs/" + hdfs_path)
    local_path = "d:/hdfs/launcher/code/chentf.zip"
    hdfs_path = local_path.replace("d:/hdfs", "")
    client.upload(hdfs_path, local_path)
    # file_continue(client, local_path, hdfs_path)

    print("ok")
