#Q3 Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.
def Addition(Num1, Num2):
    return Num1 + Num2

def Subtraction(Num1, Num2):
    return Num1 - Num2

def Multiplication(Num1, Num2):
    return Num1 *Num2

def Division(Num1, Num2):
    return Num1 / Num2

def main():
    No1 = int(input("Enter the first Number: "))
    No2 = int(input("Enter the second Number: "))

    add = Addition(No1, No2)
    print(f"{No1} + {No2} = {add}")

    sub = Subtraction(No1, No2)
    print(f"{No1} - {No2} = {sub}")
    
    mult = Multiplication(No1, No2)
    print(f"{No1} * {No2} = {mult}")
    
    div = Division(No1, No2)
    print(f"{No1} / {No2} = {div}")

if __name__ == "__main__":
    main()