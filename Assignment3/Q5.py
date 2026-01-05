# Predict the output : 

s = "Python"
print(id(s))
s = s + "3"
print(id(s))

# Line number 5 will create different new string object. 
# It does not use the same memory address of Line number 3
