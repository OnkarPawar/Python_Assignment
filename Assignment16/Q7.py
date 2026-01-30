#Q7 Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
def is_Divisible_by_5(No):
    if (No % 5) == 0:
        return True
    else:
        return False

def main():
    Number = int(input("Enter the Number: "))
    Ret = is_Divisible_by_5(Number)
    print(Ret)
    
if __name__ == "__main__":
    main()