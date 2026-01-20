#Q9 Write a lambda function which accepts two numbers and returns multiplication.
Multiplication = lambda no_1, no_2: no_1 * no_2

def main():
    No1 = int(input("Enter the First Number: "))
    No2 = int(input("Enter the Second Number: "))
    mult = Multiplication(No1, No2)
    print(mult)

if __name__ == "__main__":
    main()