import random

def genCurve(seed,max,min,incFactor,n,incWeights):
    out = []

    current = seed*random.random()
    before = 0
    
    j = 0
    while j < n:       
        inc = incFactor*(random.random() * incWeights[random.randrange(4)])

        if before >= 0:      
            current += inc
        else:
            current -= inc

        current = current if current < max else current - abs(inc)
        current = current if current > min else current + abs(inc)
       # print(current, ' ',inc)
        out.append(current)
        j += 1

    return out
