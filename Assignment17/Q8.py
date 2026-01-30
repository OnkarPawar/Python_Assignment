#Q8 Write a program which accept one number and display below pattern.
# input: 5

def Print_Pattern(No):
    for i in range(1, No + 1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
        
def main():
    Num = int(input("Enter the Number: "))
    Print_Pattern(Num)

if __name__ == "__main__":
    main()