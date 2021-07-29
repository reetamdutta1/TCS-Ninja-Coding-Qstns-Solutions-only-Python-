#0, 0, 2, 1, 4, 2, 6, 3, 8, 4, 10, 5, 12, 
#6, 14, 7, 16, 8 This series is a mixture of
#2 series all the odd terms in this series
#form even numbers in ascending order and
#every even terms is derived from the previous 
#term using the formula (x/2)

n = int(input())

a=0
b=0

for i in range(1, n+1):
    if(i%2 !=0):
        a = a +2
    else:
        b = b+ 1

if(n%2 != 0):
    print(a-2)
else:
    print(b-1)