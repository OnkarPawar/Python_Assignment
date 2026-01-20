#Q3 Write a program which accepts one number and prints factorial of that number.
def Calculate_Factorial(Num):
    Fact = 1
    for i in range(1, Num+1):
        Fact = Fact * i

    return Fact

def main():
    Number = int(input("Enter the number to calculate the factorial :"))
    Ret = Calculate_Factorial(Number)
    print(f"Factorial of {Number} is {Ret}")

if __name__ == "__main__":
    main()