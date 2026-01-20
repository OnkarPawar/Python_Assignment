#Q4 Write a program which accepts one number and prints binary equivalent.
def Calculate_Binary_Equivalent(Num):
    Binary_Equivalent = ""
    while (Num != 0):
        rem = Num % 2
        Binary_Equivalent = str(rem) + Binary_Equivalent
        Num = Num // 2
    
    return Binary_Equivalent

def main():
    Number = int(input("Enter the Number : "))
    Bin_Equivalent = Calculate_Binary_Equivalent(Number)
    print(f"Binary Equivalent of {Number} is: {Bin_Equivalent}")

if __name__ == "__main__":
    main()