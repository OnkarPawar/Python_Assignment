#Q1 Write a program which accepts one number and prints multiplication table.
def Multiplication_Table(Num):
    for i in range(1, 11):
        print(Num * i, end=" ")

def main():
    Number = int(input("Enter the Number to print the table : "))
    Multiplication_Table(Number)

if __name__ == "__main__":
    main()