import math
prim = []
def bilangan_prima(n):

    for x in range(2,n + 1):
        prima = True
        batas = int(math.sqrt(x)) + 1
        for y in range(2,batas):
            if x % y ==0:
                prima = False
                break
        if prima == True:
            prim.append(x)

n = 50
bilangan_prima(n)
print(f"Yang merupakan bilangan prima adalah {prim}")