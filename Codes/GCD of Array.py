"""
Input: N = 3, arr[] = {2, 4, 6}
Output: 2
Explanation: GCD of 2,4,6 is 2.
"""

class Solution:
    def gcd(self, n, arr):
        # code here 
        import math
        result = arr[0]
        for i in range(1,n):
            result = math.gcd(result, arr[i])
        
        return result
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.gcd(n,arr))
# } Driver Code Ends