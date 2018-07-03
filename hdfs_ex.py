#!/usr/bin/env python3
# coding=utf-8

__author__ = 'chentf'

__version__ = 'v1.0.0'

import configparser

from hdfs import InsecureClient


def download(client, hdfsPath):
    local_dir = "D:/hdfs" + hdfsPath
    client.download(hdfsPath, local_dir, overwrite=True)
    pass


def downloadTemp(client, hdfsPath, fileName):
    local_dir = "D:/hdfs/temp/" + fileName
    client.download(hdfsPath, local_dir, overwrite=True)
    pass


def uploadHdfs(client, localPath):
    hdfsPath = localPath.replace("D://hdfs/", "/")
    # client.delete(hdfsPath)
    client.upload(hdfsPath, localPath, overwrite=True)
    pass


if __name__ == '__main__':
    cf = configparser.ConfigParser()
    cf.read("config.ini")

    # hdfs = cf.get("hdfs", "hdfs_url")
    hdfs = cf.get("hdfs_test", "hdfs_url")
    client = InsecureClient(hdfs, user='hadoop')
    # client = InsecureClient(hdfs, user='hadoop')
    # client = InsecureClient(hdfs, user='dev')

    # fl = client.list("/user/dev/euler/inneralgoframefile")
    # fl = client.list("/user/dev/boss/customerfile/2018/useralgorithm/")
    # fl = client.list("/user/dev/boss/customerfile/11/")
    # fl = client.list("/user/dev/boss/customerfile/56/324555663560933382/euler/file/transform/")
    # fl = client.list("/user/dev/boss/customerfile/2018/dataset")
    # fl = client.list("/user/dev/boss/customerfile/11/10/euler/trainView/319356072888631296/")
    fl = client.list("/user/dev/boss/customerfile")
    # fl = client.list("/user/root/euler/inneralgofile")
    # client.makedirs("/launcher/code/")
    print(fl)

    # hdfspath = "/user/dev/boss/customerfile/11/10/euler/trainView/315259954451775488/model/sk.pkl"
    # hdfspath = "/user/dev/boss/customerfile/2018/dataset/train_sklearn.csv"
    # hdfspath = "/user/dev/yanhao/llbrain-taskflow-component-app-1.0.jar"
    # hdfspath = "/user/dev/euler/inneralgoframefile"
    # hdfspath = "/user/dev/llbrain-taskflow-component-app-1.0.jar"

    hdfspath = "/user/dev/boss/customerfile/3/4/euler/trainView/336406251425693696/train/algorithmParamFile/algorithmParamFile.py"
    # hdfspath = "/user/dev/boss/customerfile/56/324555663560933382/euler/file/transform/326339105780924416.csv"
    downloadTemp(client, hdfspath, "625.py")

    # localPath = "D://hdfs/user/dev/boss/customerfile/11/haha/1.txt"
    # uploadHdfs(client, localPath)
    print("ok")
