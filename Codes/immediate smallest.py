class Solution:
    def immediateSmaller(self,arr,n,x):
        #return required ans
        smallest = -1
        
        for i in arr:
            if(i>smallest and i<x):
                smallest = i
                
        if smallest != -1:
            return smallest
            
        return -1
            
            
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ =='__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(e) for e in input().split()]
        x=int(input())
        ob=Solution()
        ans=ob.immediateSmaller(arr,n,x)
        print(ans)
# } Driver Code Ends