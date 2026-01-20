#Q2 Write a program which accepts one number and print its factors.
def Print_Factors(Num):
    for i in range(1, Num + 1):
        if (Num % i) == 0:
            print(i, end=" ")

def main():
    Number = int(input("Enter the Number: "))
    Print_Factors(Number)

if __name__ == "__main__":
    main()