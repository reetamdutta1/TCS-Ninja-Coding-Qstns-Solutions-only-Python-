#input: 5 10
#output: 05 06 07 08 09 10

low = int(input("Enter starting number "))
up = int(input("Enter last number "))

c=len(str(up))

for i in range(low, up+1):
    print(str(i).zfill(c),end=" ")
    