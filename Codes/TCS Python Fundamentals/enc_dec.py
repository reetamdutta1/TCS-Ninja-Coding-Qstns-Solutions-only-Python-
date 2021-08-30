
def encode(s):
	
	# changed string
	newS = ""
	
	# iterate for every characters
	for i in range(len(s)):
		
		# ASCII value
		val = ord(s[i])
		
		#if k-th ahead character exceed 'z'
		if val + 5>122:
			newS += chr(96 + (val - 117))
			
		else:
			newS += chr(val + 5)
		
	print (newS)
			
# driver code	
str = input()

encode(str)
