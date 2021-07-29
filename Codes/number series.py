#TCS Write a Program Find the 
#nth term of the series. 1,1,2,3,4,9,8,27,16,81,32,243

#There are two consecutive sub GP’s at even and odd positions

#(GP-1) At Odd Positions (Powers of 2) – 1, 2, 4, 8, 16, 32, 64, 128
#(GP-2) At Even Positions (Powers of 3) – 1, 3, 9, 27, 81, 243, 729, 2187

num = int(input)
if(num%2==0):
    num = num//2
    print(3**(num -1))
else:
    num = num //2 + 1
    print(2**(num-1))