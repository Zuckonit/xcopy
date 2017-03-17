#coding: utf-8

import xerox
import os.path as osp
import sys

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    if osp.isfile(filename):
        with open(filename, 'rb') as f:
            xerox.copy(f.read())
