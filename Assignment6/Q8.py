#Q8. What happens if the number of arguments passed does not match the function parameters?
# Ans: Its give error: missing (number of argument) required positional argument: <parameter name>
#   it give error: takes 1 positional argument but 2 were given. 
# def EmployeeInfo():
#     pass
#         
# def main(): 
#     EmployeeInfo() 
#

def Demo(Test1):
    print (Test1)
if __name__ == "__main__":
    Demo(10,23)