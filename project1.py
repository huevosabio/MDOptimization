from singleVariable import *

def firstFunction(x, gamma=0.5):
    return (-x+(gamma*math.pow(x,2)))
    
def firstDerivative(x,gamma=0.5):
    return (-1 + (gamma*2*x))
    
optimum, value, steps = lineSearch(0,firstFunction,firstDerivative,backTracking,0.00001,1,0.5)

print optimum
print value
print steps