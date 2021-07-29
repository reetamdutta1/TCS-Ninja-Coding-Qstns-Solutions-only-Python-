#Given a maximum of 100 digit numbers as input, 
#find the difference between the sum of odd and
#even position digits

import math
num = [int(d) for d in str(input("Enter your number: "))]
even, odd = 0,0
for i in range(0, len(num)):
    if i%2 == 0:
        even = even + num[i]
    else:
        odd = odd + num[i]
print(abs(odd-even)) #absolute difference
