#Q9. What is a return value in a function?
# Ans: Its sends return value back to the caller. In function does not use return, its by default None 
#
# 
#def InfoTest():
#     return 50

# def main():
#     Result = None
#     Result = InfoTest()  
#     print("Return value is :", Result) 
    
# if __name__ == "__main__":
#     main()
def InfoTest():
    return 50

def main():
    Result = None
    Result = InfoTest()  
    print("Return value is :", Result) 
    
if __name__ == "__main__":
    main()