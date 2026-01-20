#Q5 Write a program which accepts one number and check whether it is palindrome or not
def Check_Palindrome(Num):
    Rev = 0
    while (Num != 0):
        digit = Num % 10
        Rev = Rev * 10 + digit
        Num = Num // 10
    return Rev

def main():
    Number = int(input("Enter the number: "))
    Rev_Number = Check_Palindrome(Number)
    if Rev_Number == Number:
        print(f"{Number} is palindrome")
    else:
        print(f"{Number} is not palindrome")


if __name__ == "__main__":
    main()