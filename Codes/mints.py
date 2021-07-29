s= int(input())
n= int(input())

sum =s
for i in range(1,n):
    prev = sum -1
    sum = sum + prev

print(sum)