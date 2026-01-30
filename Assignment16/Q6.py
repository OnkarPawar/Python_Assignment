#Q6 Write a program which one number from user and check whether that number is positive or negative or zero.
def CheckNum(No):
    if No > 0:
        return "Positve number"
    elif No < 0:
        return "Negative number"
    else:
        return "Zero"

def main():
    Number = int(input("Enter the Number: "))
    Ret = CheckNum(Number)
    print(Ret)
    
if __name__ == "__main__":
    main()