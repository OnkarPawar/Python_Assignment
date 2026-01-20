#Q8 Write a lambda function which accepts two numbers and returns addition.
Addition = lambda no_1, no_2: no_1 + no_2

def main():
    No1 = int(input("Enter the First Number: "))
    No2 = int(input("Enter the Second Number: "))
    add = Addition(No1, No2)
    print(add)

if __name__ == "__main__":
    main()