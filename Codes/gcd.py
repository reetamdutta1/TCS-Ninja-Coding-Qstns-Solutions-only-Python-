def gcd(x,y):
    while(y):
        x, y = y, x%y
    return x

a = int(input())
b = int(input())

print(" The GCD of the two nos. is: ", end=" ")
print(gcd(a,b))
