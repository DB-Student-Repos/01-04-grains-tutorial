def square(number):
    if(number<1 or number>64):
        print("Invalid Input")
    else:
        return 2**(number-1)
    


def total():
    #using sum of geometric series formula sum = a*(r**n - 1)/(r - 1)
    return((2**64) - 1)
