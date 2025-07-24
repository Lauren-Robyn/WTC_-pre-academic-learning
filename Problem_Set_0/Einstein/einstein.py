#here I am going define a function for the calculation
def einstein() :
    m = int(input ("enter a mass: "))
    E = m * 300000000 **2
#my function should return the value of the input multiplied by 300000000^2
    return E
print(einstein())