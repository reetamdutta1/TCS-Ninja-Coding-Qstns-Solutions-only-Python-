def find_sum_of_digits(number):
    sum=0
    for d in str(number):
        sum += int(d)
    return sum

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)
                                      