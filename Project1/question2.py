from singleVariable import *
from utilities import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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
    return firstTerm*0.1/math.pow(A, 0.9) - secondTerm/math.pow(A, 2)
    
def generate_x_y(x,y):
    #s = prob_map.shape
    x, y = np.meshgrid(x,y)
    return x.ravel(), y.ravel()

def heatmap(info_map,x,y):
    x, y = generate_x_y(x,y)
    plt.figure()
    plt.hexbin(x, y, C=info_map.ravel())
    
convergence = 0.00001

#Let's evaluate a big test space of the Line Search
x = np.arange(0.1,1,0.1)
y = np.arange(1,21,0.1)
testSpace = np.empty([x.size,y.size])
lineDict = {}
for reducParamIndex in range(x.size):
    for initStepIndex in range(y.size):
        lineDict["optimum"], lineDict["value"], lineDict["steps"], lineDict["funcEvals"] = lineSearch(0.00001,totalDrag,derTotalDrag,backTracking,0.00001,y[initStepIndex],x[reducParamIndex])
        testSpace[reducParamIndex][initStepIndex] = lineDict["funcEvals"]
    
heatmap(testSpace,x,y)
#print np.min(testSpace)
#print np.max(testSpace)
plt.axis([np.min(x-0.1), np.max(x+0.1),np.min(y-1),np.max(y+1)])
cb = plt.colorbar()
cb.set_label('Function Evaluations')
plt.ylabel("Initial Step")
plt.xlabel("Reduction Parameter")
plt.savefig('backtrackTest.png')
#print testSpace


#OK, now test the Golden Search
x = np.arange(0.1,25,0.1)
y = np.arange(30,100)
testSpace = np.empty([x.size,y.size])
goldenDict = {}
for start in range(x.size):
    for intervalSize in range(y.size):
        goldenDict["optimum"], goldenDict["minVal"], goldenDict["steps"] = goldenSearch(x[start], x[start]+y[intervalSize], totalDrag, convergence, k)
        testSpace[start][intervalSize] = goldenDict["steps"]
    
heatmap(testSpace,x,y)
plt.axis([np.min(x-0.1), np.max(x+0.1),np.min(y-1),np.max(y+1)])
cb = plt.colorbar()
cb.set_label('Function Evaluations')
plt.ylabel("Interval Size")
plt.xlabel("Starting Point")
plt.savefig('goldenTest.png')
#PRAY

#This is test code to see if the methods were converging.

lineDict = {}
goldenDict = {}

lineDict["optimum"], lineDict["value"], lineDict["steps"], lineDict["funcEvals"] = lineSearch(0.00001,totalDrag,derTotalDrag,backTracking,0.00001,10,0.2)

k =0
start = 0.000001
end = 100

goldenDict["optimum"], goldenDict["minVal"], goldenDict["steps"] = goldenSearch(start, end, totalDrag, convergence, k)

print lineDict["optimum"], lineDict["steps"], lineDict["funcEvals"]

print goldenDict["optimum"],goldenDict["minVal"], goldenDict["steps"],