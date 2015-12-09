# added by kangye python27
# -*- coding: UTF-8 -*-
def printSplit(str):
    print "---------------字符串相关操作实例----------------------------"
    head, tail = str.split(",")
    print "head is: %s, tail is: %s"%(head, tail)

def testTistsBase(list):
    print "---------------列表的基础操作实例----------------------------"
    print "input list is:", list
    print "print list[2]", list[2]
    print "print list[2:]", list[2:]
    print "print list[1:5]", list[1:5]
    del list[2]
    print "del list[2], then list is ", list
    print "len(list) ", len(list)
    print "list*2 ", list*2
    print "3 in list ", (3 in list)
    for x in list :
        print u"for x in :", x

def testListsMethod(list):
    """

    :type list: Lists
    """
    print "---------------列表的相关方法操作实例----------------------------"
    list.append(7)
    print "append:", list
    list.append(2)
    print "append 2, and count the times in list: ", list.count(2)
    #在列表末尾一次性追加另一个序列中的多个值
    list.extend([9,10, 2])
    print "extend [9, 10,2] :",list
    print "get index of 2 :",list.index(2)
    list.insert(3, [100,100])
    print "index [100,100] from index 3:", list
    del list[3]
    list.reverse()
    print "list reverse", list
    list.sort()
    print "list sort ", list
    print "pop:",list.pop()
    print "pop 2:", list.pop(2)
    print "now the list is :", list

def testListFun(list):
    print "---------------列表相关函数实例--------------------------------"

    print "sum list is :", sum(list)
    print "min list is :", min(list)
    list2 = [1,2,3,4,5,6]
    print "cmp list2 ：", cmp(list, list2)
    print "len list is ：", len(list)
    print "max list is :", max(list)

def testTupleBase(tup):
    print "--------------元组的操作和列表类似，但不同修改--------------------"
    print "the tuple is :", tup
    print "the tuple[2:]:",tup[2:]
    for x in tup :
       print "iter the :", x


def parseListAndTuple(_list, _tuple):
    print "--------------元组和列表的相互转化--------------------"
    list_ = list(_tuple)
    print "parse tuple to list :", list_
    del list_[2]
    print "now you can modify the list(del 2):", list_

    tuple_ = tuple(_list)
    print "the _list has been parsed to tuple :", tuple_

def testDictionary(dictionary_):
    print "-------------字典测试--------------------"
    print "the dictionary is :", dictionary_
    print "dictionary_['name']:", dictionary_['name']
    print "dictionary age add one is :", dictionary_['age']+1

    del dictionary_['name']
    print "del name form dictionary:", dictionary_
    dictionary_.clear()
    print "clear this dictionary :", dictionary_

def testDictionaryMethod(dictionary_):
    print "-------------字典基本方法实例--------------------"
    dictionary_['class'] = {'num':12, 'code': 'fenghou'}
    print "add other dictionary :", dictionary_

    print "str is :", str(dictionary_)
    print "type is :", type(dictionary_)

    d2 = dictionary_.copy()
    del dictionary_['name']
    print "del name from dictionary :", dictionary_
    print "d2 is(the nam of d2 is still exit) :", d2
    print "keys :",dictionary_.keys()
    print "get('sex')", dictionary_.get('sex')
    print "get('name', 'other kevin')", dictionary_.get('name', 'other kevin')
    print "items is :", dictionary_.items()
    dictionary_.setdefault('name', 'other kevin')
    dictionary_.update({'sex':'woman', 'cailer': 'enginer'})
    print "update dictionary with new dict:", dictionary_

if __name__ == "__main__":

    # 字符串常用操作
    printSplit("one,two")

    # 列表常用操作
    _list = [1,2,3,4,5,6]
    testTistsBase(_list)
    testListsMethod(_list)
    testListFun(_list)

    # 元组的通用操作
    testTupleBase((1,2,3,2))
    parseListAndTuple([1,2,3],(3,2,1))

    # 字典测试
    testDictionary({'name': 'kevin', 'age': 30, 'sex': 'man'})
    testDictionaryMethod({'name': 'kevin', 'age': 30, 'sex': 'man'})
else:
    #
    print "it is exce by other mouder"