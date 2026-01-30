# Write a program which contains filter(), map() and reduce() in it. Python application 
# which contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all prime numbers. Map function will multiply each number by 2.
# Reduce will return maximum number from that numbers.

# Input List = [21, 24, 56, 7, 5, 13, 69, 73]
# List after filter = [7, 5, 13, 73]
# List after map = [14, 10, 26, 146]
# Output of reduce = 146
from functools import reduce

def is_Prime(no):
    flag = False
    for i in range(2, no):
        if (no % i) == 0:
            flag = True
            break
    
    if flag:
        return False
    else:
        return True

def Multiply(no):
    return no * 2

def Maximum(no1, no2):
    if no1 > no2:
        return no1
    else:
        return no2

def main():
    data = []
    no_of_list_ele = int(input("Enter the Number of Elements in List: "))
    
    for i in range(no_of_list_ele):
        element = int(input(f"Enter the Value for {i} Element: "))
        data.append(element)
    
    F_Data = list(filter(is_Prime, data))    
    print(F_Data)

    Map_Data = list(map(Multiply, F_Data))
    print(Map_Data)

    Reduce_Data = reduce(Maximum, Map_Data)
    print(Reduce_Data)

if __name__ == "__main__":
    main()