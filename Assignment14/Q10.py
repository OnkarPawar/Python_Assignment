#Q10 Write a lambda function which accepts three numbers and returns largest number.
Largest_Number = lambda no_1, no_2, no_3: (no_1 if no_1 > no_2 and no_1 > no_3 else no_2 if no_2 > no_3 else no_3)

def main():
    No1 = int(input("Enter the First Number: "))
    No2 = int(input("Enter the Second Number: "))
    No3 = int(input("Enter the Third Number: "))
    Largest_No = Largest_Number(No1, No2, No3)
    print(Largest_Number)

if __name__ == "__main__":
    main()