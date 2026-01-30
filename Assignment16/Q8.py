#Q8 Write a program which number from user and print that number of "*" on screen.
def Print_Star(No):
    for i in range(No):
        print("*", end=" ")

def main():
    number = int(input("Enter the Number: "))
    Print_Star(number)

if __name__ == "__main__":
    main()