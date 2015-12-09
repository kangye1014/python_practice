#!/usr/bin/python
# -*- coding: UTF-8 -*-
# added by kangye python27

import time
import calendar

def getTime():
    ticks = time.time()
    print "Number of ticks since 12:00am, January 1, 1970:", ticks

    localtime = time.localtime(time.time())
    print "Local current time :", localtime

    localtime = time.asctime( time.localtime(time.time()) )
    print "Local current time :", localtime

def testCal():
    cal = calendar.month(2015, 12)
    print "Here is the calendar:"
    print cal;



if __name__ == "__main__":

    # 时间测试
    getTime()

    testCal()
else:
    #
    print "it is exce by other mouder"
