def min(a,b):
    if a<=b:
        return a
    return b

def max(a,b):
    if a>=b:
        return a
    return b


def gcd(a,b):
    if a==0:
        return b
    ans = 1
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i == 0:
            ans = i
    return ans

def lcd(a,b):
    if a == 0 :
        return b
    multi = a*b
    return (int)(multi/gcd(a,b))


trap = input()
if trap == "sum":
    ans = 0
    while(True):
        t = input()
        if t == "end":
            break
        ans += int(t)
    print(ans)
elif trap == "average":
    ans = 0
    n = 0
    while(True):
        t = input()
        if t == "end" :
            break
        ans += int(t)
        n += 1

    myFloat = round(ans/n,2)
    print(myFloat)
elif trap == "lcd":
    ans = 0
    while(True):
        t = input()

        if t == "end" :
            break
        ans = lcd(ans ,int(t))

    print(ans)

elif trap == "gcd":
    ans = 0

    while(True):
        t = input()

        if t == "end" :
            break
        ans = gcd(ans ,int(t))


    print(ans)

elif trap == "min":
    ans = 1e12
    while(True):
        t = input()

        if t == "end" :
            break
        ans = min(ans,int(t))
    print(ans)

elif trap== "max":
    ans = -1e12
    while(True):
        t = input()

        if t == "end" :
            break
        ans = max(ans,int(t))
    print(ans)
else:
    print("Invalid command")


