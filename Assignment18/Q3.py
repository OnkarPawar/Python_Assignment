
#Q3 Write a program which accept N numbers from user and store it into List. Returns minimum number from that list
# Input: Number of element: 4
# Input Elements: 453 63 564 23
# Output: 23


def Min_Element(l):
    Max_No = l[0]
    for i in range(len(l)):
        for j in range(i + 1 , len(l)):
            if l[j] < Max_No:
                Max_No = l[j]

    return Max_No

def main():
    No_of_Elements = int(input("Enter the Number of Element: "))
    l1 = []

    for i in range(No_of_Elements):
        val = int(input(f"Enter the {i} element value: "))
        l1.append(val)

    result = Min_Element(l1)
    print("Input Elements: ", l1)
    print("Minimum Element from List is: ", result)

if __name__ == "__main__":
    main()

