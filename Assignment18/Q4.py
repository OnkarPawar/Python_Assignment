#Q4 Write a program which accept N numbers from user and store it into List. 
# Accept one another number from user and return frequency of that another number.
# Input: Number of element: 4
# Input Elements: 453, 63, 453, 23, 67
# Element to Search: 453
# Output: 2
# 

def Frequency_of_Element(l, search):
    cnt = 0
    for i in range(len(l)):
        if l[i] == search:
            cnt += 1

    return cnt

def main():
    No_of_Elements = int(input("Enter the Number of Element: "))
    l1 = []

    for i in range(No_of_Elements):
        val = int(input(f"Enter the {i} element value: "))
        l1.append(val)

    search = int(input("Enter the number that you want to search in List: "))
    result = Frequency_of_Element(l1, search)
    print("Input Elements: ", l1)
    print("Search Element: ", search)
    print(f"Frequency of {search} is: {result}")

if __name__ == "__main__":
    main()

