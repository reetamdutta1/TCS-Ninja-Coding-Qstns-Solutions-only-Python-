Given a non-negative number n. The problem is to find the smallest number k such that the product of digits of k is equal to n. If no such number k can be formed then print “-1”.
Examples: 
 

Input : 100
Output : 455
4*5*5 = 100 and 455 is the
smallest possible number.

Input : 26
Output : -1

#User function Template for python3

def smallestK(n):
    # code here
    # retured value will be printed by driver code
    if (n>=0 and n<=9): #if n is a single digit number
        return n
    digits = list() #store the digits in stack
    for i in range(9,1,-1):
        while(n%i==0):
            
            digits.append(i)
            n=n//i
       
    if (n!=1):
        return -1
        
    k = 0
    while(len(digits)!=0):
        k = k*10+digits[-1]
        digits.pop()
        
    return k


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        print(smallestK(n))

# } Driver Code Ends