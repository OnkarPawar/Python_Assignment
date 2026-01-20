#Q4 Write a program which accepts one number and prints cube of that number.
def Calculate_Cube(No):
    return No ** 3

def main():
    Number = int(input("Enter the Number to calculate the cube: "))
    Cubed_Number = Calculate_Cube(Number)
    print("Cube of", Number, "is", Cubed_Number)

if __name__ == "__main__":
    main()