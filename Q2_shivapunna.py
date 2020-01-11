"""Stack MIn: How would you design a stack which, in addition to push and pop, has a function min which returns
the minimum element? Push, po and min should all operate in O(1) time"""

import random


class Stack:
    def __init__(self):
        self.__stack = list()

    def push(self, value):
        self.__stack.append(value)

    def top(self):
        try:
            return self.__stack[-1]
        except IndexError:
            return None

    def pop(self):
        try:
            return self.__stack.pop()
        except IndexError:
            return None


class StackMin:
    def __init__(self):
        self.__s1 = Stack()
        self.__s2 = Stack()

    def push(self, data):
        self.__s1.push(data)
        if self.__s2.top() is None:
            self.__s2.push(data)
        elif data <= self.__s2.top():
            self.__s2.push(data)
        else:
            pass

    def pop(self):
        if self.__s2.top() == self.__s1.top():
            self.__s2.pop()
            return self.__s1.pop()
        else:
            return self.__s1.pop()

    def top(self):
        return self.__s1.top()

    def min(self):
        return self.__s2.top()


if __name__ == '__main__':
    n = 5
    InputNumbers = [random.randint(1, n*10) for i in range(0, n)] + [0]
    print("input:", InputNumbers)
    sm = StackMin()
    for i in InputNumbers:
        sm.push(i)

    print("Minimum element",sm.min())
    sm.pop()
    print("After first pop", sm.min())









