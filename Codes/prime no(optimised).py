#{ 
#Driver Code Starts
#Initial Template for Python 3

import math


 # } Driver Code Ends
#User function Template for python3

class Solution:
    def isPrime(self,N):
        # code here
        
        if N > 1:

        	for i in range(2, int(math.sqrt(N))+1):
        
        		
        		if (N % i== 0):
        			return False
        			break
        	else:
        		return True
        
        else:
        	return False

#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        
        ob=Solution()
        if(ob.isPrime(N)):
            print("Yes")
        else:
            print("No")
        T-=1
    
    
if __name__=="__main__":
    main()
#} Driver Code Ends