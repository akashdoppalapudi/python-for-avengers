from math import sqrt
t = int(input())

for _ in range(t):
    n = int(input())
    factorsum = 1

    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            factorsum += i
            if i!=int(sqrt(n)):
                factorsum += n//i

    if factorsum==n:
        print("YES")
    else:
        print("NO")