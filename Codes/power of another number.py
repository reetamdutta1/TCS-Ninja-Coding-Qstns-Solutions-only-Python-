#Given two positive numbers X and Y, check if Y is a power of X or not.

class Solution:
    def isPowerOfAnother (ob,X,Y):
        # code here
        # The only power of 1 
        # is 1 itself 
        if (X == 1): 
            if (Y == 1) :
                return 1
            else:
                return 0
              
        # Repeatedly compute 
        # power of x 
        pow = 1
        while (pow < Y): 
            pow = pow * X 
      
        # Check if power of x 
        # becomes y 
        if (pow == Y) :
            return 1
        else:
            return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        X,Y=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.isPowerOfAnother(X,Y))
# } Driver Code Ends