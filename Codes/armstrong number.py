#Armstrong number
#153 = 1*1*1 + 5*5*5 + 3*3*3
#153 is an Armstrong number.

num = int(input())
sum = 0

temp = num #storing the actual number given by the user
while temp>0:
    digit = temp%10
    sum += digit **3
    temp //=10

#display result
if num ==sum:
    print("This ia an Armstrong number")
else:
    print("This is not an Armstrong number")

