import math

def backTracking(initStep, reducParam, objectiveFunc, pk, derivObjFunc, currentGuess,u1 = 0.0001):
    step = initStep
    while (objectiveFunc(currentGuess + step*reducParam) > (objectiveFunc(currentGuess)+(u1*pk*derivObjFunc(currentGuess)*step))):
        print (objectiveFunc(currentGuess + initStep*reducParam))
        print ((objectiveFunc(currentGuess)+(u1*pk*derivObjFunc(currentGuess)*step)))
        step = step*reducParam
    return step


def lineSearch(initGuess, objectiveFunc, derivObjFunc, stepFunc, convergence, initStep, reducParam):
    delta = convergence+1
    k = 0
    currentGuess = initGuess
    while (delta > convergence):
        print currentGuess
        pk = (-derivObjFunc(currentGuess))/(math.fabs(derivObjFunc(currentGuess)))
        step = stepFunc(initStep, reducParam, objectiveFunc, pk, derivObjFunc, currentGuess)
        dummy = currentGuess
        currentGuess = currentGuess + (step*pk)
        delta = math.fabs(objectiveFunc(currentGuess)-objectiveFunc(dummy))
        k = k +1
    return currentGuess, objectiveFunc(currentGuess),k