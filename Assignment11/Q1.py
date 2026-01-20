#Q1 Write a program which accepts one number and checks whether it is prime or not.
flag = False

def Check_Prime(Num):
    global flag
    for i in range(2, Num):
        if (Num % i) == 0:
            flag = True
            break

def main():
    global flag
    Number = int(input("Enter the number to check whether it is prime or not : "))
    Check_Prime(Number)
    if flag:
        print(f"{Number} is not prime")
    else:
        print(f"{Number} is prime")

if __name__ == "__main__":
    main()