import random

def genCurve(seed,max,min,incFactor,n):
    out = []

    current = seed*random.random()

    j = 0
    while j < n:       
        inc = incFactor*(random.random() * [-1,1][random.randrange(2)])

        current += inc
        current = current if current < max else current - abs(inc)
        current = current if current > min else current + abs(inc)
       # print(current, ' ',inc)
        out.append(current)
        j += 1

    return out
#genCurve(0.9,1,0,0.1,100)
