str_1 = input("entrez des lettres")
str_2 = input("entrez upper / lower / title ou clean")


def my_upper():
   print(str_1.upper())


def my_lower():
    print(str_1.lower())


def my_title():
    list1= str_1.split(' ')
    for i in range (len(list1)):
       list1[i] = list1[i].capitalize()

    str = " ".join(list1)
    print(str)


def my_clean():
    print(str_1.replace(' ', ''))


if str_2 == "upper":
    my_upper()
elif str_2 == "lower":
    my_lower()
elif str_2 == "title":
    my_title()
elif str_2 == "clean":
    my_clean()
else:
    print("entrez upper / lower / title ou clean")