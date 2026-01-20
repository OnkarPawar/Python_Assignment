#Q4 Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.
#from functools import reduce
import functools

Add = lambda no1, no2 : no1+no2

def main():
    Data = [7, 22, 52, 45, 6, 23, 26, 12, 28, 38]
    print("Given Data is: ", Data)

    Reduce_Data = functools.reduce(Add, Data)
    print("Data after addition of each numbers: ", Reduce_Data)

if __name__ == "__main__":
    main()