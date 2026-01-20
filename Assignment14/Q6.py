#Q6 Write a lambda function which accepts one number and returns True if number is odd otherwise False.
is_Odd = lambda no: (True if no%2 != 0 else False)
def main():
    Number = int(input("Enter the Number: "))
    Check_Odd = is_Odd(Number)
    print(Check_Odd)

if __name__ == "__main__":
    main()