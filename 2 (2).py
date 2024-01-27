def nCr(n,i):
    t = factor(i)*factor(n-i)
    return (int)(factor(n)/t)

def factor(n):
    a = 1
    for i in range(2,n+1):
        a *= i
    return a



n = int(input())
# nCr method:
for i in range(n):
    for j in range(i+1):
        print(nCr(i,j) , end= " ")
    print()
