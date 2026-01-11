#Q3. Explain the use of the global keyword. When should it be used?
#Ans: 
#   To modifying a global variable, use a golbal keyword .#   
# 

x = 100
def Fun ():
    global x
    x = x + 1
    print(x)
Fun()    