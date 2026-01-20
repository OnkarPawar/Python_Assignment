#Q4 Write a program which accepts one number and prints that many numbes staring from 1.
def Print_That_Many_Numbers(Num):
    for i in range(1, Num + 1):
        print(i, end=" ")

def main():
    Number = int(input("Enter the number: "))
    Print_That_Many_Numbers(Number)

if __name__ == "__main__":
    main()