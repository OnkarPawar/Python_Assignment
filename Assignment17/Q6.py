#Q6 Write a program which accept one number and display below pattern.
# input: 5

def Print_Pattern(No):
    while (No != 0):
        print("*  " * No)
        No = No - 1

def main():
    Num = int(input("Enter the Number: "))
    Print_Pattern(Num)

if __name__ == "__main__":
    main()