Geek and his classmates are playing a prank on their Computer Science teacher. They change places every time the teacher turns to look at the blackboard. Each of the N students in the class can be identified by a unique roll number X and each desk has a number i associated with it. Only one student can sit on one desk. Each time the teacher turns her back, a student with roll number X sitting on desk number i gets up and takes the place of the student with roll number i. If the current position of N students in the class is given to you in an array, such that i is the desk number and a[i] is the roll number of the student sitting on the desk, can you modify a[ ] to represent the next position of all the students ?
Example 1:
  N = 6
  a[ ] = {0, 5, 1, 2, 4, 3}
  Output: 0 3 5 1 4 2
  Explanation: After reshuffling, the modified position of all the students would be {0, 3, 5, 1, 4, 2}.
Example 2:
  N = 5
  a[ ] = {4, 3, 2, 1, 0}
  Output: 0 1 2 3 4
  Explanation: After reshuffling, the modified position of all the students would be {0, 1, 2, 3, 4}.
➔ Your Task: You dont need to read input or print anything. Complete the function prank() which takes the array a[ ] and its size N as input parameters and modifies the array in-place to reflect the new arrangement.

#User function Template for python3

class Solution:
	def rearrange(self, array, n):
		#code here
		for i in range(n):
            array[i] = array[i] + (array[array[i]] % n) * n

        for i in range(n):
            array[i] = array[i] // n


#{ 
#  Driver Code Starts


if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        array = list(map(int, input().strip().split(' ')))
        ob = Solution()
        ob.rearrange(array,n)
        for i in array:
            print(i,end=" ")
        print()
# } Driver Code Ends