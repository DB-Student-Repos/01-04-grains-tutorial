#def square(number):
#    if(number<1 or number>64):
#        raise ValueError("square must be between 1 and 64")
#    else:
#        return 2**(number-1)
    


#def total():
#    #using sum of geometric series formula sum = a*(r**n - 1)/(r - 1)
#    return((2**64) - 1)

def square(number):
    if (number<1 or number>64):
        raise ValueError ("square must be between 1 and 64")
    else:
        grain = 2**(number-1)
        return grain

def total():
    return (18446744073709551615)
