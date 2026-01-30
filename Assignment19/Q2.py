# Write a program which contains one lambda function which accepts two parameter and return it's multiplication.
# Input: 5  4                Output: 20
# Input: 7  7                Output: 49

Multi_of_Two = lambda no1, no2: no1 * no2

def main():
    Number_1 = int(input("Enter the  First Number: "))
    Number_2 = int(input("Enter the Second Number: "))
    Result = Multi_of_Two(Number_1, Number_2)
    print(f"{Number_1} * {Number_2} = {Result}")

if __name__ == "__main__":
    main()