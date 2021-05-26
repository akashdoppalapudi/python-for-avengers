numRows = int(input())

pt = []

for i in range(1,numRows+1):
    arr = [1 for j in range(i)]
    pt.append(arr)

for i in range(2,numRows):
    for j in range(1, len(pt[i])-1):
        pt[i][j] = pt[i-1][j-1] + pt[i-1][j]


print(pt)