def CheckPrime(No):
    flag = False
    for i in range(2, No):
        if (No % i) == 0:
            flag = True
            break
    
    if flag:
        return False
    else:
        return True 