import re

response = int(input("Comptera le nombre de mots de la taille renseigné du fichier data.txt: "))
file = open("data.txt", "rt")
data = file.read()
words = data.split()
count = 0
for i in range (0,len(words)):
    if len(words[i]) == response:
        count +=1

print(count)