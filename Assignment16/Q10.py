#Q10 Write a program which accept name from user and display length of its name.
def Len_of_Name(Name):
    return len(Name)

def main():
    Name = input("Enter the Name: ")
    Ret = Len_of_Name(Name)
    print(f"Length of {Name} is: {Ret}")

if __name__ == "__main__":
    main()