#Q4 Write a program which accepts one number and prints all even numbers till that number.
def Print_All_Even_Number(Num):
    for i in range(2, Num+1):
        if (i % 2) == 0:
            print(i, end=" ")

def main():
    Number = int(input("Enter the number : "))
    Print_All_Even_Number(Number)

if __name__ == "__main__":
    main()