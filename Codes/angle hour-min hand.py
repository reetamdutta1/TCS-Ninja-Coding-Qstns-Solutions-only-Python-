class Solution:
    def getAngle(self, H , M):
        # code here
        if H ==12:
            H=0
        if M == 60:
            M=0
            
        hour_ang = 0.5 * (H*60+M)
        min_ang = 6*M
        
        angle = abs(hour_ang - min_ang)
        
        if(angle>180):
            angle = int(360 - angle)
            
        else:
            angle = int(angle)
            
        return angle
        
        
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        H,M=map(int,input().split())
        
        ob = Solution()
        print(ob.getAngle(H,M))
# } Driver Code Ends