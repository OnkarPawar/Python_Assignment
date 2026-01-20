#Q8 Write a lambda funtion using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.
is_Divisible = lambda no: (no % 3 == 0 and no % 5 == 0)

def main():
    Data = [7, 22, 52, 45, 6, 23, 26, 12, 28, 38]
    print("Given data is:", Data)

    Filter_Data = list(filter(is_Divisible, Data))
    print("List of numbers which is divisible by 3 and 5: ", Filter_Data)

if __name__ == "__main__":
    main()