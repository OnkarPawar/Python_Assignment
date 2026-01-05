
def Addition():
    No1 = 10
    No2 = 11
    Ans = 0
    Ans = No1 + No2
    return Ans

def Subtraction():
    No1 = 50
    No2 = 11
    Ans = 0
    Ans = No1 - No2
    return Ans

def Multiplication():
    No1 = 4
    No2 = 5
    Ans = 0
    Ans = No1 * No2
    return Ans

def Division():
    No1 = 16
    No2 = 4
    Ans = 0
    Ans = No1 / No2
    return Ans

def main():
    Result1 = 0
    Result2 = 0
    Result3 = 0
    Result4 = 0

    Result1 = Addition()
    print("Addition of two number is : ", Result1)

    Result2 = Subtraction()
    print("Substraction of two number is : ", Result2)

    Result3 = Multiplication()
    print("Multiplication of two number is : ", Result3)

    Result4 = Division()
    print("Division of two number is : ", Result4)

# Starter
if __name__ == "__main__":
    main()