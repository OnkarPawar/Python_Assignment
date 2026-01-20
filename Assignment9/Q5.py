#Q5 Write a program which accepts one number and check whether it is divisible by 3 and 5.
def Check_Divisible(No):
    if (No % 3) == 0 and (No % 5) == 0:
        return True

def main():
    Val = int(input("Enter the Number : "))
    Ret = Check_Divisible(Val)
    if Ret:
        print(Val, "is divisible by 3 and 5")
    else:
        print(Val, "is not divisible by 3 and 5")


if __name__ == "__main__":
    main()