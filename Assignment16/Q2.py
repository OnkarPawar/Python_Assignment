#Q2 Write a program which contains one function named as ChkNum() which accepts one parameter as numbre. If number is even then it should disply "Even number" otherwise display "Odd number" on console.
def CheckNum(No):
    if (No % 2) == 0:
        return "Even number"
    else:
        return "Odd number"

def main():
    Number = int(input("Enter the Number: "))
    Ret = CheckNum(Number)
    print(Ret)
    
if __name__ == "__main__":
    main()