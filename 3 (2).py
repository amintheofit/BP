n = int(input())

a = []
b=[]
for i in range(n):
    e = input()
    a.append(e.split('@')) if "@" in e else a.append([e,''])

for j in a:
    b.append(j[1])

b = list(set(b))
b.sort()

for k in b:
    print(k)
    

