class Solution:
    def factorial (self, N):
        # code here
        ans = 1
        for i in range(2,N+1):
            ans = ans*i
            
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.factorial(N))

# } Driver Code Ends