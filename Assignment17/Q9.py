#Q9 Write a program which accept number from user and return number of digits in that number
# 5187934           output:7

def Count_of_Digits(Num):
    cnt = 0
    while (Num != 0):
        cnt = cnt + 1
        Num = Num // 10
    return cnt

def main():
    Number = int(input("Enter the number: "))
    Ret = Count_of_Digits(Number)
    print("Count of digits is:", Ret)

if __name__ == "__main__":
    main()