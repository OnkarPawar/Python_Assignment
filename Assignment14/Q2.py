#Q2 Write a lambda function which accepts one number and returns cube of that number.
Calculate_Cube = lambda no: no ** no

def main():
    Number = int(input("Enter the Number to calculate the cube: "))
    Cubed_Number = Calculate_Cube(Number)
    print("Cube of", Number, "is", Cubed_Number)

if __name__ == "__main__":
    main()