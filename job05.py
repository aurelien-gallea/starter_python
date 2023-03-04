nb1_int = int(input("entrez votre 1er nombre"))
nb2_int = int(input("entrez votre 1er nombre"))

if nb1_int == nb2_int:
    print("valeurs égales")
else :
    for i in range (nb1_int+1, nb2_int) :
        print(i)