#Q6. Can a function return another function? Explain conceptually.
# Ans: Yes, firstly create one function (Add) with pass 1 variable, in this function create one more function for Addition logic. Return Addition for Add function 
# #

def Add(x):
    def Addition(n):
        return n + x    
    return Addition  # We return the function itself

double = Add(2)

print(double(5))