input_list = [10,20,30,'x','abc',40,'i']
output_list = [i**2 for i in input_list if isinstance(i,int)]
print(output_list)