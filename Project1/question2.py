from singleVariable import *
from utilities import *

#Get Total drag as function of A

k = 1.2
p = 1.23
u = 17.8*math.pow(10, -6)
V = 35
S = 11.8
Swet = 2.05*S
Cl = 0.3
e = 0.96
#Reynold's number divided by A
Re = (p*V*math.sqrt(S))/u
#Cf without the A component
Cf = 0.074/(math.pow(Re, 0.2))
#First Term without A (should be multiplied by A^0.1)
firstTerm = k*Cf*(Swet/S) #equals 0.00752
#Second Term without A (should be divided by A)
secondTerm = math.pow(Cl, 2)/(math.pi*e) #equals 0.0298

def totalDrag(A):
    return firstTerm*math.pow(A, 0.1) + secondTerm/A

def derTotalDrag(A):
    return firstTerm*math.pow(A, -0.9) - secondTerm/math.pow(A, 2)

convergence = 0.00001

lineDict = {}
goldenDict = {}

lineDict["optimum"], lineDict["value"], lineDict["steps"], lineDict["funcEvals"] = lineSearch(0.00001,totalDrag,derTotalDrag,backTracking,0.00001,10,0.9)

k =0
start = 0.000001
end = 100

goldenDict["optimum"], goldenDict["minVal"], goldenDict["steps"] = goldenSearch(start, end, totalDrag, convergence, k)

print lineDict["optimum"], lineDict["steps"]

print goldenDict["optimum"],goldenDict["minVal"], goldenDict["steps"]