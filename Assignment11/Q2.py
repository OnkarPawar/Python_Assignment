#Q2 Write a program which accepts one number and prints count of digits in that number.
def Count_of_Digits(Num):
    cnt = 0
    while (Num != 0):
        cnt = cnt + 1
        Num = Num // 10
    return cnt

def main():
    Number = int(input("Enter the number : "))
    Ret = Count_of_Digits(Number)
    print("Count of digits is:", Ret)

if __name__ == "__main__":
    main()