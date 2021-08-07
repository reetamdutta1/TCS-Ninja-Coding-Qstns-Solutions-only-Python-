class Solution:
    def trappingWater(self, arr,n):
        #Code here
        # To store the maximum water
        # that can be stored
        res = 0
         
        # For every element of the array
        for i in range(1, n - 1) :
             
            # Find the maximum element on its left
            left = arr[i];
            for j in range(i) :
                left = max(left, arr[j])
             
            # Find the maximum element on its right
            right = arr[i]
             
            for j in range(i + 1 , n) :
                right = max(right, arr[j])
                 
            # Update the maximum water
            res = res + (min(left, right) - arr[i])
     
        return res;

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends