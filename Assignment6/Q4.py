#Q4. Differentiate between calling a function and defining a function with a simple explanation.
#Ans: Defining a function means creating the function by naming it and writing the logic that performs a specific operation for the user.
#     Calling a function means triggering its execution to perform its task and retrieve the resulting output.
#Eg.
# def EmployeeInfo():
#     print("I am calling function")
#         
# def main(): #Called function
#     EmployeeInfo() #correct 
#

def main():     #Called function
    print("Calling function")
    
if __name__ == "__main__":  #Calling 
    main()