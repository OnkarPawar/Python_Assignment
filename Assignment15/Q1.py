#Q1 Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.
Square = lambda no : (no * no)

def main():
    Data = [7, 22, 52, 45, 6, 23, 26, 12, 28, 38]
    print("Given Data is: ", Data)

    Map_Data = list(map(Square, Data))
    print("Data after calculate of each number is: ", Map_Data)

if __name__ == "__main__":
    main()