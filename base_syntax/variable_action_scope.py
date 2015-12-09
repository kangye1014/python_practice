#!/usr/bin/python
# -*- coding: UTF-8 -*-
# added by kangye python27

import data_type
from utils import *

sex = 20
author = data_type.author
def testLocalVar():
    name = 'hello'
    # global sex
    sex = 30
    print locals()
    print  globals()
    return;

if __name__ == "__main__":

    testLocalVar()
    print sex
    print dir()
    print __file__
    print Math.add(2,3)
    print DateUtil.printTime()
    #data_type.printSplit("hello, kevin")
else:
    #
    print "it is exce by other mouder"