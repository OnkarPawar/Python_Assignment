
def Add(Value1, value2):
    #Result = 0
    Result = Value1 + value2
    return Result

def Subtraction(Value1, value2):
    #Result = 0
    Result = Value1 - value2
    return Result

def Multiplication(Value1, value2):
    #Result = 0
    Result = Value1 * value2
    return Result

def Division(Value1, value2):
    Result = 0.0
    Result = Value1 / value2
    return Result

def main():
    No1 = 0
    No2 = 0
   
    No1 = int(input("Enter first Num :" ))
    No2 = int(input("Enter Second Num :" ))
    Result_Add = Add(No1, No2)
    Result_Sub = Subtraction(No1, No2)
    Result_Multiplication = Multiplication(No1, No2)
    Result_Division = Division(No1, No2)
    print("Addition is :", Result_Add)
    print("Subtractiontion is :", Result_Sub)
    print("Multiplicationtion is :", Result_Multiplication)
    print("Division is :", Result_Division)

if __name__ == "__main__":
    main()
    

#Result1 = 21
#Result2 = 21

# Result1 = [21]
# Result2 = [21]
 
# print("Result value is: ", Result1, Result2)
# print("Type of Result variable: ",type(Result1))
# print("Type of Result variable: ",type(Result2))
# print("Memory Address of Result variable: ", id(Result1))
# print("Memory Address of Result variable: ", id(Result2))
# print(sys.getsizeof(Result1))
# print(sys.getsizeof(Result2))
# print(id(Result1) == id(Result2))
