#Q1 Write a lambda function which accepts one number and returns squre of that number.
Calculate_Square = lambda no: no * no

def main():
    Val = int(input("Enter the Number to calculate the square: "))
    Ret = Calculate_Square(Val)
    print("Square of", Val, "is", Ret)

if __name__ == "__main__":
    main()