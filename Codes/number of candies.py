n=int(10)
k = int(input())

if(k==0):
    print("Invalid input")
    print("Number of candies available = ", n)
else:
    print("Candies sold: ", k)
    print("Candies available: ", n-k)