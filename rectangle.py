x = int(input("donnez la largeur"))
y = int(input("donnez la hauteur"))

line = "-"
wall = "|"
space = " "

for i in range (1,y+1):
    if i == 1 or i == y:
        print(wall + (line*2) * x + wall)
    else:
        print((wall + (space*2) * x + wall))