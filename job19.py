import collections
from collections import deque
def func(*args):
    print("myList")
    data = deque(args)

    mySort = []

    for i in range(len(data)):
        mySort.append(min(data))
        data.remove(min(data))

    print(mySort)
func(6,2,0,4,1)