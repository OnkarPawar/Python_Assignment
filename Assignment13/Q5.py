#Q5 Write a program which accepts marks and display grade
def Display_Grade(Mark):
    if Mark >= 75:
        return "Distinction"
    elif Mark >= 60:
        return "First Class"
    elif Mark >= 50:
        return "Second Class"
    elif Mark < 50:
        return "Fail"

def main():
    Mark = int(input("Enter the Mark: "))
    Grade = Display_Grade(Mark)
    print(Grade)

if __name__ == "__main__":
    main()