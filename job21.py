import collections
from collections import deque
myList = []


def mySort(*args):
    print("myList")
    data = deque(args)

    for i in range(len(data)):
        myList.append(min(data))
        data.remove(min(data))

    return myList


def display(list):
    print(list)


mySort(6,2,0,4,1)
display(myList)
