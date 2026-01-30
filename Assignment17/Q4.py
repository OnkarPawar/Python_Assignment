#Q4 Write a program which accept one number from user and return addition of its factors.
# input: 12     Output: 16   (1+2+3+4+6)

def Factor_Sum(No):
    Fact_Sum = 0
    for i in range(1, No):
        if (No % i) == 0:
            Fact_Sum = Fact_Sum + i
    return Fact_Sum

def main():
    Number = int(input("Enter the number: "))
    Ret = Factor_Sum(Number)
    print("Addition of factors is: ", Ret)

if __name__ == "__main__":
    main()