#Q4 Write a lambda function which accepts two number and returns minimum number.
Min_Number = lambda no_1, no_2: (no_1 if no_1 < no_2 else no_2)

def main():
    No1 = int(input("Enter the First Number: "))
    No2 = int(input("Enter the Second Number: "))
    Min_No = Min_Number(No1, No2)
    print(Min_No)

if __name__ == "__main__":
    main()