#Q3 Write a program which accept one number from user and return it's factorial.
# input: 5          output: 120

def Factorial(No):
    fact = 1
    while (No!=0):
        fact = fact * No
        No = No - 1
    return fact

def main():
    Number = int(input("Enter the Number:"))
    Ret = Factorial(Number)
    print(f"factorial of {Number} is: {Ret}")

if __name__ == "__main__":
    main()