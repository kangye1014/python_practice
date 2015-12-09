#!/usr/bin/python
# -*- coding: UTF-8 -*-
# added by kangye python27

class Person:
    "人的基本类型"
    # 申明类属性
    name = ""
    age  = 0
    # 私有属性
    __sex = "man"

    # 构造方法
    def __init__(self, name, age , sex="man"):
        self.name = name
        self.age  = age
        self.__sex = sex

    def display(self):
        self.__ageCount(3)
        print "this man name is %s , and age is %d , and sex is %s"%(self.name, self.age, self.__sex)
        return self

    def getAge(self):
        return self.age

    def getSex(self):
        return self.__sex

    # 私有方法
    def __ageCount(self, i):
        self.age += i

class Man(Person):
    "男人"

    power = 10

    def __init__(self, power, name):
        self.power = power
        self.name  = name

    # 方法覆盖
    def display(self):
        print "the name is %s, the age is %d"%(self.name, self.age)
        return self

    def getAge(self):
        print "调用子类"
        self.age += 7
        return self.age

if __name__ == "__main__":

    persona = Person("kangye",12)
    print persona.name

    # 链式编程
    print persona.display().getAge()
    print persona.getSex()

    personb = Person("kangye",12,"handsome boy!")
    personb.display()

    mana = Man(100, "kevin !")
    print mana.age
    print mana.display().getAge()
