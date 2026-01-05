# a = 10
# b = 10

# and

a = [10]
b = [10]

print("Memory address of a is : ", id(a))
print("Memory address of b is : ", id(b))


# Explanation 
# When we assigning values like below then it used same menory,
# because the values are same and we are not assigning list
# a = 10
# b = 10


# But when we assigning values like below then it used different menory,
# because the values are same but the lists are different. And the different list taken different memory
# a = [10]
# b = [10]