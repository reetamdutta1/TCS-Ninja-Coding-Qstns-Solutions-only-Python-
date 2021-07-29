def celsius(temp):
    celsius = (temp - 32)*(5/9)
    return(celsius)

def fahr(temp):
    fahrenheit = (temp * 9/5) + 32
    return(fahrenheit)

print("50 degree fahrenheit in Celsius is: ",celsius(50))
print("50 degree Celsius in fahrenheit is: ",fahr(50))