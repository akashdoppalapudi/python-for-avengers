import time
from linkedList import Node

arr = [2,4,6,5,3,8,7,9,12,14,15]
root = Node().convert(arr)

key = 5

st = time.time()
for i in range(len(arr)):
    if arr[i] == key:
        print(key,"is found at index", i)
        break
else:
    print(key,"is not found")
et = time.time()

print("Runtime =", et-st)

st = time.time()
node = root
i = 0
while node!=None:
    if node.val == key:
        print(key,"is found at position", i)
        break
    node = node.next
    i += 1
else:
    print(key,"is not found")

et = time.time()
print("Runtime =", et-st)


st = time.time()
try:
    print(key,"is found at index", arr.index(key))
except ValueError:
    print(key, "is not found")
et = time.time()
print("Runtime =", et-st)