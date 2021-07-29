#input: 5 10
#output: 05 06 07 08 09 10

low = int(input())
up = int(input())

for i in range(low, up+1):
    if up>=100:
        print("{:03d}".format(i), end =" ")
    elif(up>=10):
        print("{:02d}".format(i), end =" ")
    else:
        print(i, end =" ")
