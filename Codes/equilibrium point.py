#Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
#Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        sum = 0
        for i in range(0,N):
            sum +=A[i]

        sum2 = 0
        for i in range(0, N, +1):
            sum -= A[i]

            if sum2 == sum:
                return(i+1) #index of equilibrium point

            sum2 += A[i]
        return -1
#{ 
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
