import random

def genCurve(seed,max,min,incFactor,n,incWeights, *args, **kwargs):
    spike = kwargs.get('spike', None)
    spikeFactor = kwargs.get('spikeFactor', 0)
    out = []

    current = seed*random.random()
    before = 0
    
    j = 0
    while j < n:       
        j += 1
        inc = incFactor*(random.random() * incWeights[random.randrange(4)])

        if before >= 0:      
            current += inc
        else:
            current -= inc
        
        if (spike):
            if (j % spike == 0):
                print("spike!")
                current *= spikeFactor

        current = current if current < max else current - abs(inc)
        current = current if current > min else current + abs(inc)
        current = current if current >= min else min
        current = current if current <= max else max
       # print(current, ' ',inc)
        out.append(current)


    return out
