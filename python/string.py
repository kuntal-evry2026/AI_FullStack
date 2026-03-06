first = "hello"
second = "world"

result = first + "" +second
print (result)



name ="Alice"
age = 25
print ("My name is "+name+" and i am "+str(age)+"years old")

#split()
sentence = "Validate that the Employee ID shown in the result matches the stored dynamic variable"
words = sentence.split()
print(words)
    
#join()
joined_sentence = " ".join(words)
print(joined_sentence)

#replace()
rep_sentence = sentence.replace("Employee ID", "EmpID")
print(rep_sentence)