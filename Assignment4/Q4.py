# Predict the output:
ba = bytearray([65,66,67])
ba[0] = 97
print(ba)   # bytearray(b'aBC')

# Why is this allowed?
# => In line number 3 we have modified the 0th index value. 
# And it can be happen because bytearray is mutable.
