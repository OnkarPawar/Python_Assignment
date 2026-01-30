#Q5 Write a program which accept one number from user and check whether number is prime or not.
# Input: 5       Output: It is prime NUmber

def is_Prime(No):
    Flag = False
    for i in range(2, No):
        if (No % i) == 0:
            Flag = True
            break
    
    if Flag:
        return "It is not prime number"
    else:
        return "It is prime number"

def main():
    Number = int(input("Enter the Number:"))
    Ret = is_Prime(Number)
    print(Ret)

if __name__ == "__main__":
    main()