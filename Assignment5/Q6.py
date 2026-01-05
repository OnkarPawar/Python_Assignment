import sys

# Write a program to display:
# Data type
# Memory Address
# Size in bytes 
# of a variable entered by user

def Display(Name):
    print("Data type : ", type(Name))
    print("Memory Address : ", id(Name))
    print("Size in bytes : ", sys.getsizeof(Name))

def main():
    print("Enter name : ")
    Name = input()
    Display(Name)

# Starter
if __name__ == "__main__":
    main()