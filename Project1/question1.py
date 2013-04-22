from singleVariable import *
from utilities import *

gammaValues = [0.5, 10, 10000]
gammaDict = {}
newtonDict = {}

def make_obj_function(gamma):
    def _function(x):
        return (-x+(gamma*math.pow(x,2)))
    return _function

def make_der_function(gamma):
    def _function(x):
        return (-1 + (gamma*2*x))
    return _function

def make_second_der(gamma):
    def _function(x):
        return 2*gamma
    return _function

def to_string(floating):
    if type(floating) is float:
        return str.format('{0:.6f}', floating)
    else:
        return str(floating)
    
for gamma in gammaValues:
    #print gamma
    firstFunction = make_obj_function(gamma)
    firstDerivative = make_der_function(gamma)
    secondDerivative = make_second_der(gamma)
    
    gammaDict[gamma] = {}
    gammaDict[gamma]["optimum"], gammaDict[gamma]["value"], gammaDict[gamma]["steps"], gammaDict[gamma]["funcEvals"] = lineSearch(0,firstFunction,firstDerivative,backTracking,0.00001,1,0.5)
    #print gammaDict[gamma]["optimum"]
    
    newtonDict[gamma] = {}
    newtonDict[gamma]["optimum"], newtonDict[gamma]["value"], newtonDict[gamma]["steps"], newtonDict[gamma]["funcEvals"] = newtonMethod(0,firstFunction,firstDerivative, secondDerivative, 0.00001)

text = "Backtrack LineSearch: \n"
for gammaValue in gammaDict:
    text = text + "Gamma = " + to_string(gammaValue) + "\n"
    for key in gammaDict[gammaValue]:
        text = text + to_string(key) + " = " + to_string(gammaDict[gammaValue][key]) + "\n"
    text= text + "\n\n"

text = text +"\n\n\n"

text = text + "Newton's method: \n"
for gammaValue in newtonDict:
    text = text + "Gamma = " + to_string(gammaValue) + "\n"
    for key in newtonDict[gammaValue]:
        text = text + to_string(key) + " = " + to_string(newtonDict[gammaValue][key]) + "\n"
    text= text + "\n\n"

save_txt("question1.txt", text)
print "done!!"