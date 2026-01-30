#Q9 Write a program which display first 10 even numbers in screen.
def First_10_Even_No():
    Count = 0
    Even = 2

    while Count < 10:
        print(Even, end=" ")
        Even += 2
        Count += 1


def main():
    First_10_Even_No()

if __name__ == "__main__":
    main()