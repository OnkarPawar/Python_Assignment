#Q2 Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
def CheckGreater(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2

def main():
    no_1 = int(input("Enter the First Number: "))
    no_2 = int(input("Enter the Second Number: "))
    greater_number = CheckGreater(no_1, no_2)
    print(greater_number, "is greater")

if __name__ == "__main__":
    main()