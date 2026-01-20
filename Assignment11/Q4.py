#Q4 Write a program which accepts one number and prints reverse of that number
def Print_Reverse_Number(Num):
    Rev = 0
    while (Num != 0):
        Digit = Num % 10
        Rev = Rev * 10 + Digit
        Num = Num // 10
    return Rev

def main():
    Number = int(input("Enter the number: "))
    print("Original Number:", Number)
    Rev_Number = Print_Reverse_Number(Number)
    print("Reverse Number:", Rev_Number)

if __name__ == "__main__":
    main()