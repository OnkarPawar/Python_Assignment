import sys
#Result1 = 21
#Result2 = 21

Result1 = [21]
Result2 = [21]
 
print("Result value is: ", Result1, Result2)
print("Type of Result variable: ",type(Result1))
print("Type of Result variable: ",type(Result2))
print("Memory Address of Result variable: ", id(Result1))
print("Memory Address of Result variable: ", id(Result2))
print(sys.getsizeof(Result1))
print(sys.getsizeof(Result2))
print(id(Result1) == id(Result2))
