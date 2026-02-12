def kuadrat(a,b):
    hasil = 1
    for x in range(b, 0, -1):
        if x == 0:
            print(hasil)
        else:
            hasil *= a
    
    return hasil

print(kuadrat(2,5))
