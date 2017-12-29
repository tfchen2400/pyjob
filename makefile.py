#!/usr/bin/env python3
# coding=utf-8
import os

__author__ = 'chentf'

__version__ = 'v1.0.0'


def generatorFile(size):
    file = open("d:/chentf", "w")
    file.seek(1024 * 1024 * 1024 * size)
    file.write('\x00')
    file.close()
    get_FileSize("d:/chentf")


def generatorFileTwo(size, path):
    file = open(path, "w")
    n = 0
    while True:
        n = n + 1
        temp = str(n) + "-abcdefghijklmnopqistuvwxyz" + "\n"
        for i in range(0, 1024):
            temp_inner = str(i) + "-" + temp
            file.write(temp_inner)
        if (get_FileSize(path) > size * 1024):
            break
    print(get_FileSize(path))


# 单位为MB
def get_FileSize(filePath):
    filePath = unicode(filePath, 'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    fsize_num = round(fsize, 2)
    print("size" + str(fsize_num))
    return fsize_num


if __name__ == '__main__':
    # generatorFile(200)
    generatorFileTwo(0.1, "d:/love.txt")
