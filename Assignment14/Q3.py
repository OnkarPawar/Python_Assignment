#Q3 Write a lambda function which accepts two number and returns maximum number.
Max_Number = lambda no_1, no_2: (no_1 if no_1 > no_2 else no_2)

def main():
    No1 = int(input("Enter the First Number: "))
    No2 = int(input("Enter the Second Number: "))
    max_no = Max_Number(No1, No2)
    print(max_no)

if __name__ == "__main__":
    main()