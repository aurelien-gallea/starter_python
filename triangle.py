x = int(input("entrez la hauteur"))

space = " "
l_wall = "/"
r_wall = "\ "
base = "_"

for i in range (1,x+1):

    print(space * (x+1-i) + l_wall + space * ((i-1)*2) + r_wall)
    if i == x :
        print(l_wall + base * (x*2) + r_wall)