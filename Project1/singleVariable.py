from __future__ import division
import math


def backTracking(initStep, reducParam, objectiveFunc, pk, derivObjFunc, currentGuess,u1 = 0.0001):
    step = initStep
    funcEvals = 0
    #print "this is my pk"
    #print pk
    #print "this is my thing to beat"
    #print (objectiveFunc(currentGuess)+(u1*pk*derivObjFunc(currentGuess)*step))
    #print "and this is what I have"
    #print objectiveFunc(currentGuess + step*reducParam)
    while (objectiveFunc(currentGuess + step*reducParam) > (objectiveFunc(currentGuess)+(u1*pk*derivObjFunc(currentGuess)*step))):
        #print (objectiveFunc(currentGuess + initStep*reducParam))
        #print ((objectiveFunc(currentGuess)+(u1*pk*derivObjFunc(currentGuess)*step)))
        step = step*reducParam
        #print "Step within function:"
        #print step
        funcEvals += 1
    return step, funcEvals


def lineSearch(initGuess, objectiveFunc, derivObjFunc, stepFunc, convergence, initStep, reducParam):
    delta = convergence+1
    k = 0
    currentGuess = initGuess
    funcEvals = 0
    currentEvaluation = objectiveFunc(currentGuess)
    currentDerivative = derivObjFunc(currentGuess)
    
    while (delta > convergence):
        #print "current guess:"
        #print currentGuess
        #print delta

        #protect from zero division
        if (currentDerivative) == 0:
            currentDerivative = 0.00000000001
        #Evaluate step
        pk = (-currentDerivative)/(math.fabs(currentDerivative))
        step, stepEvals = stepFunc(initStep, reducParam, objectiveFunc, pk, derivObjFunc, currentGuess)
        #print "This is my step:"
        #print step
        funcEvals = stepEvals + funcEvals
        
        #Update guess
        dummy = currentGuess
        currentGuess = currentGuess + (step*pk)
        delta = math.fabs(objectiveFunc(currentGuess)-objectiveFunc(dummy))
        
        #Evaluate function and save values
        currentEvaluation = objectiveFunc(currentGuess)
        currentDerivative = derivObjFunc(currentGuess)
        #print "DERIVATIVE: "
        #print currentDerivative
        k = k +1
        if k > 9:
            break
    return currentGuess, objectiveFunc(currentGuess),k, funcEvals
    
def newtonMethod(initGuess, objectiveFunc, firstDerivative, secondDerivative, convergence):
    currentGuess = initGuess
    currentEval = objectiveFunc(currentGuess)
    currentDerivative = firstDerivative(currentGuess)
    currentSecondDer = secondDerivative(currentGuess)
    funcEvals = 1
    delta = convergence+1
    k = 0
    while (delta > convergence):
        #protect divide by zero
        if (currentSecondDer == 0):
            currentSecondDer = 0.00000000001
        
        #Evaluate new step
        #print currentGuess, currentEval, currentDerivative
        newGuess = currentGuess - (currentDerivative/currentSecondDer)
        #print newGuess
        delta = math.fabs(newGuess-currentGuess)
        #print delta
        
        #TODO: fail to get good steping procedure...
        
        #Switcharoo
        currentGuess = newGuess
        currentEval = objectiveFunc(currentGuess)
        currentDerivative = firstDerivative(currentGuess)
        currentSecondDer = secondDerivative(currentGuess)
        k += 1
        funcEvals +=1
    return currentGuess, currentEval, k, funcEvals
    
def goldenSearch(start, end, objectiveFunc, convergence, k):
    k += 1
    #print k
    left = (end-start)*(1-0.618) + start
    right = (end-start)*(0.618) + start
    leftEval = objectiveFunc(left)
    rightEval = objectiveFunc(right)
    #print math.fabs(leftEval-rightEval) 
    if math.fabs(leftEval-rightEval) < convergence:
        if min([leftEval, rightEval]) == leftEval:
            return left, leftEval, k
        else:
            return right, rightEval, k
    elif leftEval < rightEval:
        return goldenSearch(start, right, objectiveFunc,convergence, k)
    else:
        return goldenSearch(left, end, objectiveFunc, convergence, k)
