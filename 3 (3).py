a = input().split()

b = {}

for i in a :
    
    digits = ""
    characters = ""

    for char in i:
        if char.isdigit():
            digits += char
        else:
            characters += char
    
    b[int(digits)] = characters

c = ''

for i in range(len(a)):
    c += b[i]

print(c)