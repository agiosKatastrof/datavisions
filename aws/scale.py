import random

def genWeight(scaleFactor, scaleRange):
    weights = []
    for i in scaleRange:
        weights += [scaleFactor * i] * i
    return random.choice(weights)
