str_1 = input("entrez un seul mot sans accents ni majuscule")
# 97/122 min 65/90

array_word = []

for i in range(1,len(str_1)):
    array_word.append(str_1[i])


array_word.sort()

s = array_word
d = ''.join(s)

new_word = str_1[0] + d
print(new_word)


