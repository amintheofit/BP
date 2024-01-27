n = int(input())
cols , rows = (n,1000000)
arr = [["." for i in range(cols)] for j in range(rows)]
arr[0][0] = "*"
i = 0
j = 0
line = 0
while(True):
    inp = input()
    line += 1

    if inp == "R":

        if j < cols:
            j = j+1
            arr[i][j] = "*"
    elif inp == "L":

        if j != 0:
            j = j-1
            arr[i][j] = "*"
    elif inp == "B":
        i = i+1
        arr[i][j] = "*"

    if inp == "END":
        break


for k in range(i+1):
    for q in range(n):
        print(arr[k][q] , end = "")
    print()
if j != n-1:
    print("!There's no way out")



