#Q2 Write a program which accepts radium of circle and prints area of circle.
PI = 3.142

def Calculate_Area_of_Circle(r):
    return PI * (r * r)

def main():
    Radius = float(input("Enter the radius of circle: "))
    Area_of_Circle = Calculate_Area_of_Circle(Radius)
    print("Area of Circle is: ", Area_of_Circle)

if __name__ == "__main__":
    main()