#Q9 Write a lambda funtion using filter() which accepts a list of numbers and returns the product of all elements.
import functools

Product_Element = lambda a, b: a * b

def main():
    Data = [15, 35, 55, 72]
    print("Given Data is:", Data)

    Reduce_Data = functools.reduce(Product_Element, Data)
    print("Product of all elements in List is:", Reduce_Data)

if __name__ == "__main__":
    main()
