#Q3 Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
def Add(No_1, No_2):
    return No_1 + No_2

def main():
    Number1 = int(input("Enter the First Number: "))
    Number2 = int(input("Enter the Second Number: "))
    Ret = Add(Number1, Number2)
    print(f"Addition of {Number1} + {Number2} = {Ret}")
    
if __name__ == "__main__":
    main()