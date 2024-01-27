import math
def len(li):
    ans = 0
    for x in li:
        ans += 1
    return ans

def divider(n):
    ans = 0
    for i in range(1,n + 1):
        if  n%i == 0:
            ans += i
    return ans
def changeBase(n , b):
    myList = []

    while(n>0):
        myList.append(n%b)
        n = int(n/b)
    myList = myList[::-1]
    return myList


li = []
while(True):
    n,b = input().split()
    if  n == "-1" and b == "-1":
        break
    n = int(n)

    b = int(b)
    ans = 0
    basedNumber = changeBase(divider(n) , b)
    for i in range(len(basedNumber)):
        ans += basedNumber[i]*math.pow(10 , len(basedNumber) - i - 1)
    ans = int(ans)
    li.append(ans)
ans = 0
for x in li:
    ans += x
print(ans)

