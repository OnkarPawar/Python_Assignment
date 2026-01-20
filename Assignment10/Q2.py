#Q2 Write a program which accepts one number and prints sum of first N natural number.
def Sum_of_First_n_Natural_Numbers(Num):
    Sum = 0
    while (Num != 0):
        Sum = Sum + Num
        Num =Num - 1
    return Sum

def main():
    Number = int(input("Enter the number to print the sum of first N natural numbers: "))
    Sum_of_Num = Sum_of_First_n_Natural_Numbers(Number)
    print("Sum of first N natural numbers is:", Sum_of_Num)
    
if __name__ == "__main__":
    main()