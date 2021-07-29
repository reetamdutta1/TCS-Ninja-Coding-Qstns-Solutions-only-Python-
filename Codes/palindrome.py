#string/number palindrome

user = input()
str1 = "".join(reversed(user))

if user==str1:
    print("Palindrome")
else:
    print("Not a Palindrome")