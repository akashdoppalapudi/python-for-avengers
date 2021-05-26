s = input().strip()

k = ''
for i in s:
    if i.isalnum():
        k = k+i
k = k.lower()


if k == k[::-1]:
    print(True)
else:
    print(False)