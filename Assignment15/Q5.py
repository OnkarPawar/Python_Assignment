#Q5 Write a lambda function using reduce() which accepts a list of numbers and returns the maximum elements.
from functools import reduce

Max_Element = lambda a, b: a if a > b else b

def main():
    Data = [7, 22, 52, 45, 6, 23, 26, 12, 28, 38]
    print("Given Data is:", Data)

    Reduce_Data = reduce(Max_Element, Data)
    print("Maximum element in List is:", Reduce_Data)

if __name__ == "__main__":
    main()
