import time
arr = list(map(int, input().split()))
key = int(input())

st = time.time()
for i in range(len(arr)):
    if arr[i] == key:
        print(key,"is found at index", i)
        break
else:
    print(key,"is not found")
et = time.time()
print("Runtime :",et-st)

st = time.time()
try:
    print(key,"is found at index", arr.index(key))
except ValueError:
    print(key, "is not found")
et = time.time()
print("Runtime =", et-st)

arr.sort()

st = time.time()              #binarySearch
lptr = 0
rptr = len(arr) - 1
while(lptr<=rptr):
    mid = (lptr+rptr)//2
    if arr[mid] == key:
        print(key,"is found at index", mid)
        break
    elif arr[mid] > key:
        rptr = mid-1
    else:
        lptr = mid+1
else:
    print(key, "is not found.")
et = time.time()
print("Runtime :",et-st)