import math
X="123456"
d=2

accum = "123456"
def section():
    y= 0
    for x in X:
    
        y = y+1
    newy = math.floor(y /2)
    for x in range(newy):
        newsec = accum[d:2*d-1]

        print(newsec)

    print(y)

section()
