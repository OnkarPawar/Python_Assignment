#Q3 Write a program which accepts one number and prints square of that number.
def Calculate_Square(No):
    return No * No

def main():
    Val = int(input("Enter the Number to calculate the square: "))
    Ret = Calculate_Square(Val)
    print("Square of :", Val, "is", Ret)

if __name__ == "__main__":
    main()