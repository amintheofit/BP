a = input()

h = []

at = False
has = False

for i in range(len(a)):
    if a[i] == "@":
        at = True
    if a[i] == "#" and at == True :
        h.append(i)
        at = False
        has = False

if len(h) > 0:
    for j in range(len(h)):
        a = a[:h[j]-j] + a[h[j]-j+1:] 
        
q = len(a)-1
w = 0

for i in range(q):
    if a[i - w] == ' ' and a[i - w+1] == ' ':
        a = a[:i- w] + a[i- w+1:]
        w+=1

print(f"Formatted Text: {a}")
