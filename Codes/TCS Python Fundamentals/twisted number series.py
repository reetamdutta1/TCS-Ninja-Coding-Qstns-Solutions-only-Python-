# 0,0,7,6,14,12,18,28...

n = int(input())
a=0
b=0

for i in range(1,n+1):
    if i%2!=0:
        a=a+7
    else:
        b=b+6

if n%2!=0:
    print(a-7)
else:
    print(b-6)
