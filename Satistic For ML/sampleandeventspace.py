from itertools import product

#sample space of dice tool 

sample_space = list(range(1,7))

#probability of rolling a even number 

even_numbers = [2,4,6]

probability_of_even_number = len(even_numbers) /len (sample_space)

print("P-even :" ,probability_of_even_number)

