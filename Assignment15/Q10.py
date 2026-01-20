#Q10 Write a lambda funtion using filter() which accepts a list of numbers and returns the count of even numbers.
is_Odd = lambda no: (no % 2 == 0)

def main():
    Data = [7, 22, 52, 45, 6, 23, 26, 12, 28, 38]
    print("Given data is:", Data)

    Filter_Data = len(list(filter(is_Odd, Data)))
    print("Count of even numbers is:", Filter_Data)

if __name__ == "__main__":
    main()