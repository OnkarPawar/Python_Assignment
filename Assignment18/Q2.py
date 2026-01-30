
#Q2 Write a program which accept N numbers from user and store it into List. Returns maximum number from that list
# Input: Number of element: 4
# Input Elements: 234 3 456 876
# Output: 876


def Max_Element(l):
    Max_No = l[0]
    for i in range(len(l)):
        for j in range(i + 1 , len(l)):
            if l[j] > Max_No:
                Max_No = l[j]

    return Max_No

def main():
    No_of_Elements = int(input("Enter the Number of Element: "))
    l1 = []

    for i in range(No_of_Elements):
        val = int(input(f"Enter the {i} element value: "))
        l1.append(val)

    result = Max_Element(l1)
    print("Input Elements: ", l1)
    print("Maximum Element from List is: ", result)

if __name__ == "__main__":
    main()

