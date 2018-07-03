#!/usr/bin/env python3
# coding=utf-8

__author__ = 'chentf'

__version__ = 'v1.0.0'

import os
import re


def removeComment(f):
    input = open(f, encoding="utf-8")
    all_the_text = input.read()
    input.close()
    all_the_text2 = re.subn("#.*#", '', all_the_text)
    outputName = os.path.split(f)
    outputName = os.path.join(os.getcwd(), "pro", outputName[1])
    output = open(outputName, "w")
    output.write(all_the_text2[0])
    output.close()


def pro_file(path):
    needProFile = []

    files = os.listdir(path)
    for f in files:
        needProFile.append(os.path.join(path, f))
    for f in needProFile:
        removeComment(f)
    print(needProFile)


if __name__ == '__main__':
    path = os.path.join(os.getcwd(), "template")
    pro_file(path)
