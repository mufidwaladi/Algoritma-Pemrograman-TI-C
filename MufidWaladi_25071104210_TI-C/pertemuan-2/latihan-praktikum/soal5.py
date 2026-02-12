import math

def jarak(x1,y1,x2,y2):
    total = 0
    X = (x2 - x1)**2
    Y = (y2 - y1)**2
    total = math.sqrt(X + Y)
    print(total)
x1,y1,x2,y2 = (7,6,3,3)
jarak(x1,y1,x2,y2)