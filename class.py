#!/usr/bin/python

class ClassTest:
    def __init__(self):
        self.a=2
    def geta(self):
        return self.a
def test():
    test=ClassTest()
    print getattr(ClassTest,'a','not found')
    print getattr(ClassTest,'b','not gound')
    print getattr(test,'','not gound')
    print test.geta()

if __name__=='__main__':
    test()
