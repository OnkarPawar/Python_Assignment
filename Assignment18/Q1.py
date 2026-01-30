
#Q1 Write a program which accept N numbers from user and store it into List. Returns addition of all elements from that List.
# Input: Number of element: 4
# Input Elements: 23 54 11 51
# Output: 139


def Sum_Elements(No):
    Sum = 0
    for i in range(len(No)):
        Sum = Sum + No[i]

    return Sum

def main():
    No_of_Elements = int(input("Enter the Number of Element: "))
    Num = []

    for i in range(No_of_Elements):
        val = int(input(f"Enter the {i} element value: "))
        Num.append(val)

    result = Sum_Elements(Num)
    print("Addition of List Elements is: ", result)

if __name__ == "__main__":
    main()

