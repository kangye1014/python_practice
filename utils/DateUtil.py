#!/usr/bin/python
# -*- coding: UTF-8 -*-
# added by kangye python27

import  datetime
import  time

def printTime():
    localtime = time.localtime(time.time())
    print "Local current time : ", localtime
    return