#Q1 Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input: 4                  output: 16
# Input: 6                  Output: 64

Power_of_Two = lambda no: (2 ** no)

def main():
    Number = int(input("Enter the Number: "))
    Result = Power_of_Two(Number)
    print(Result)

if __name__ == "__main__":
    main()