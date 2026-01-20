#Q3 Write a program which accepts one number and prints sum of digits.
def Sum_of_Digits(Num):
    Digit_Sum = 0
    while (Num != 0):
        digit_sum = digit_sum + Num % 10
        Num = Num // 10
    return digit_sum

def main():
    Number = int(input("Enter the number : "))
    Ret_Digit_Sum = Sum_of_Digits(Number)
    print("Sum of digits is:", Ret_Digit_Sum)

if __name__ == "__main__":
    main()