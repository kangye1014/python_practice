# added by kangye python27

def printSplit(str):
    head, tail = str.split(",")
    print "head is: %s, tail is: %s"%(head, tail)

def testTists(list):
    print "input list is:", list
    print "print list[2]", list[2]
    print "print list[2:]", list[2:]
    print "print list[1:5]", list[1:5]
    del list[2]
    print "del list[2], then list is ", list

if __name__ == "__main__":

    # 字符串常用操作
    printSplit("one,two")

    list = [1,2,3,4,5,6]
    testTists(list)

else:
    #
    print "it is exce by other mouder"