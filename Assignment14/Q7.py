#Q7 Write a lambda function which accepts one number and returns True if number is divisible by 5.
Check_Divisible = lambda no: (True if (no % 5 == 0) else False)

def main():
    Val = int(input("Enter the Number: "))
    Ret = Check_Divisible(Val)
    print(Ret)

if __name__ == "__main__":
    main()