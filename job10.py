txt = input("entrez du texte")

file = open("output.txt", "w")
file.write(txt)
file.close()

file = open("output.txt", "r")
print(file.read())
file.close()