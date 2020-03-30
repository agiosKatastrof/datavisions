import random

def genWeight(scaleFactor, scaleRange):
    weights = []
    for i in scaleRange:
        weights += [scaleFactor * i] * i
    return random.choice(weights)

def boundaryScale(scaleFactor,scaleRange,inN):

    scaledN = []
    normN = []

    for i in inN:
    
        weight = genWeight(scaleFactor,scaleRange)
        i *= weight
        scaledN.append(i)

    m = max(scaledN)
    for j in scaledN:
        normN.append(j/m)

    return normN
