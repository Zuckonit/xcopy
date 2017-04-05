#coding: utf-8

import xerox
import codecs
import os.path as osp
import sys

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    if osp.isfile(filename):
        with codecs.open(filename, 'rb', encoding='utf-8') as f:
            xerox.copy(f.read())
