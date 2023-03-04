def func(*args):
    print("myList")

    data = []
    for i in range(len(args)):
       data.append(args[i])

    data.sort()

    print(data)


func(6,2,0,4,1)