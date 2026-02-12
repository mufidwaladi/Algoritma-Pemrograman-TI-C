def penambahan(a,b):
    return a + b

def pengurangan(a,b):
    return a - b

def perkalian(a,b):
    return a*b

def pembagian(a,b):
    if b == 0 :
        print("Pembagian tidak dapat dilakukan karena pembagi bernilai 0")
    else:
        return a / b

def modulus(a,b):
    return a % b


print(penambahan(9,3))
print(pengurangan(9,3))
print(pembagian(9,3))
print(modulus(9,3))

