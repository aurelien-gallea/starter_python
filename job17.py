def func(*args):
    print("myList")
    for i in range(0, len(args)):
        if args[i] % 2 == 0:
            print(args[i])

func(1,2,3,4,5,6)