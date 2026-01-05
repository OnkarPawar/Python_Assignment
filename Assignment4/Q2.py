# Predict the output
b = bytes([65,66,67])

print(b)    # output : b'ABC'

# Explain how numbers are converted internally
# The bytes() constructor iterates through the list [65, 66, 67]. 
# Each integer is treated as a single byte of data. 
# Python interprets these byte values based on the ASCII encoding


