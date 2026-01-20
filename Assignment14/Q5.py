#Q5 Write a lambda function which accepts one number and returns True if number is even otherwise False.
is_Even = lambda no: (True if no%2 == 0 else False)
def main():
    Number = int(input("Enter the Number: "))
    Check_Even = is_Even(Number)
    print(Check_Even)

if __name__ == "__main__":
    main()