# What is a user defined function?
# => User defined function means which is written by user or programer.

def Multiplication(Value1, Value2):
    return Value1 * Value2

def main():
    No1 = 0
    No2 = 0
    Result = 0
    print("Enter first value : ")
    No1 = int(input())
    print("Enter second value : ")
    No2 = int(input())
    Result = Multiplication(No1, No2)
    print("Multiplication is : ", Result)

# Starter
if __name__ == "__main__":
    main()