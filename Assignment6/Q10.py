#Q9. Can a Python function return multiple values? If yes, how does Python handle it internally?
# Ans: Yes, its in tuple packing/unpacking return vaule.
# #
# 
#def OrderDetails(O_Id, P_Name, Price):
#     print("Order Details : ", O_Id, P_Name, Price)
#     return "Return Multiple value",21,45.50

# def main():
#     Result1 = None
#     Result2 = None
#     Result3 = None
    
#     Result1, Result2,Result3 = OrderDetails(001,"Laptop", 30000.60 )  
#     print("Return value are :", Result1, Result2, Result3)
    
# if __name__ == "__main__":
#     main()

def OrderDetails(O_Id, P_Name, Price):
    print("Order Details : ", O_Id, P_Name, Price)
    return "Return Multiple value",21,45.50

def main():
    Result1 = None
    Result2 = None
    Result3 = None
    
    Result1, Result2,Result3 = OrderDetails(10054,"Laptop", 30000.60 )  
    print("Return value are :", Result1, Result2, Result3)
    
if __name__ == "__main__":
    main()