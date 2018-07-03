#!/usr/bin/env python3
# coding=utf-8

__author__ = 'chentf'

__version__ = 'v1.0.0'
import ast

if __name__ == '__main__':
    s = "[{\"num_outputs\":32,\"type\":\"conv\",\"kernel_size\":[5,5]},{\"type\":\"max_pool\",\"kernel_size\":\"[2,2]\"},{\"num_outputs\":64,\"type\":\"conv\",\"kernel_size\":[5,5]},{\"type\":\"max_pool\",\"kernel_size\":[\"2\",\"2\"]},{\"type\":\"flatten\"},{\"num_outputs\":1024,\"type\":\"fully_connected\"},{\"num_outputs\":10,\"activation_fn\":None,\"type\":\"fully_connected\"}]"
    print(s)
    d = ast.literal_eval(s)
    print(type(d))
    print(d)
