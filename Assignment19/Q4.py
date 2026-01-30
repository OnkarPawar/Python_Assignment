#Q4 Write a program which contains filter(), map() and reduce() in it. Python application 
# which contains one list of numbers. List contains  the numbers which are accepted from user.
# Filter should filter our all such numbers which are even.
# Map function will calculate it's square. Reduce will return addition of all that numbers.
# Enter the Number of Elements in List: 9
# Input List = [21, 24, 56, 67, 89, 90, 44, 55, 77]
# List after filter = [24, 56, 90, 44]
# List after map = [576, 3136, 8100, 1936]
# Output of reduce = 13748

from functools import reduce

Even_Filter = lambda no: no % 2 == 0

Square_Map = lambda no: no * no

Addition_Reduce = lambda no1, no2: no1 + no2

def main():
    data = []
    no_of_list_ele = int(input("Enter the Number of Elements in List: "))
    
    for i in range(no_of_list_ele):
        element = int(input(f"Enter the Value for {i} Element: "))
        data.append(element)
    
    f_data = list(filter(Even_Filter, data))    
    print(f_data)

    map_data = list(map(Square_Map, f_data))
    print(map_data)

    reduce_data = reduce(Addition_Reduce, map_data)
    print(reduce_data)

if __name__ == "__main__":
    main()