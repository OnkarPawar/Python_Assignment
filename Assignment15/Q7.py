#Q7 Write a lambda funtion using filter() which accepts a list of strings and returns a list of strings having length greater than 5
String_Len_Grt_Five = lambda string: (len(string) > 5)

def main():
    Data = ["Om", "Nam_Shivay", "Jay", "Shri_Ram", "Jay_Shivray"]
    print("Given data is:", Data)

    Filter_Data = list(filter(String_Len_Grt_Five, Data))
    print("List of strings having length greater then 5:", Filter_Data)

if __name__ == "__main__":
    main()