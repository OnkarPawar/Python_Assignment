#Q3 Write a program which accepts one number and checks whether it is peferct number or not.
def Check_Perfect(Num):
    Sum_of_Div = 0
    for i in range(1, Num):
        if (Num % i) == 0:
            Sum_of_Div = Sum_of_Div + i
    return Sum_of_Div

def main():
    Number = int(input("Enter the Number: "))
    is_Perfect = Check_Perfect(Number)
    if is_Perfect == Number:
        print(f"{Number} is perfect number")
    else:
        print(f"{Number} is not perfect number")

if __name__ == "__main__":
    main()