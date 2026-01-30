#Q2 Write a program which accept one number and display below pattern.
# input: 5

def Print_Pattern(no):
    for i in range(no):
        print("*  " * no)

def main():
    no = int(input("Enter the Number: "))
    Print_Pattern(no)

if __name__ == "__main__":
    main()