#Q5 Write a program which accept N numbers from user and store it into List. 
# Returns addition of all prime numbers from that list. Main python file 
# accepts N numbers from user and pass each number to ChkPrime() function which is
# part of our user defined module named as MarvellousNum. Name of the function from python file should ListPrime().  
# Input: Number of element: 6
# Input Elements: 23, 7, 5, 55, 78, 90
# Output: (23 + 7 + 5) = 35

import MarvellousCheckPrimeNum as checkprime

def ListPrime(l):
    Sum_of_Prime = 0
    for i in range(len(l)):
        is_prime = checkprime.CheckPrime(l[i])
        if is_prime:
            Sum_of_Prime = Sum_of_Prime + l[i]
        
    return Sum_of_Prime


def main():
    No_of_Elements = int(input("Enter the Number of Element: "))
    Num = []

    for i in range(No_of_Elements):
        val = int(input(f"Enter the {i} element value: "))
        Num.append(val)

    Result = ListPrime(Num)
    print("Input Elements: ", Num)
    print("Addition of all prime numbers from list is: ", Result)

if __name__ == "__main__":
    main()
