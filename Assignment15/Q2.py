#Q2 Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.
is_Even = lambda no: (no % 2 == 0)

def main():
    Data = [7, 22, 52, 45, 6, 23, 26, 12, 28, 38]
    print("Given data is:", Data)

    Filter_Data = list(filter(is_Even, Data))
    print("Data after filter is: ", Filter_Data)

if __name__ == "__main__":
    main()