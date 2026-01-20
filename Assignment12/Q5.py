#Q5 Write a program which accepts one number and prints that many numbers in reverse order.
def Print_That_Many_Numbers_Rev_order(Num):
    while (Num != 0):
        print(Num, end=" ")
        Num = Num - 1

def main():
    Number = int(input("Enter the number: "))
    Print_That_Many_Numbers_Rev_order(Number)

if __name__ == "__main__":
    main()