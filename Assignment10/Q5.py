#Q5 Write a program which accepts one number and prints all odd numbers till that number.
def Print_All_Odd_Number(Num):
    for i in range(Num + 1):
        if (i % 2) != 0:
            print(i, end=" ")

def main():
    Number = int(input("Enter the number: "))
    Print_All_Odd_Number(Number)

if __name__ == "__main__":
    main()