#Q1 Write a program which accepts length and width of rectangle and prints area.
def Calculate_Area_Of_Rectangle(Length, Width):
    return Length * Width

def main():
    Length_Value = float(input("Enter the length: "))
    Width_Value = float(input("Enter the width: "))
    ret = Calculate_Area_Of_Rectangle(Length_Value, Width_Value)
    print(ret)

if __name__ == "__main__":
    main()