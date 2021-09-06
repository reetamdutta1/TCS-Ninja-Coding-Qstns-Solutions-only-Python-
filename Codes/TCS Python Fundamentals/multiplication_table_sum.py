n = int(input("Enter the number: "))
value = 0
sum = 0

for i in range(1,11):
    value = n*i
    print(n," x ", i, " = ", value)
    sum = sum + value

print("The sum is: ", sum)


