#Q6 Write a lambda function using reduce() which accepts a list of numbers and returns the minimum elements.
import functools

Min_Element = lambda a, b: a if a < b else b

def main():
    Data = [7, 22, 52, 45, 6, 23, 26, 12, 28, 38]
    print("Given Data is:", Data)

    Reduce_Data = functools.reduce(Min_Element, Data)
    print("Manimum element in List is:", Reduce_Data)

if __name__ == "__main__":
    main()
