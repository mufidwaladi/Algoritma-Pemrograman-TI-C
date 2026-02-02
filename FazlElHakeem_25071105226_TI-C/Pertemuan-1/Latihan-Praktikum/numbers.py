#ada tiga tipe data numerik di python:
#  *int
#  *float
#  *complex

#-Int-
#int atau integer adalah bilangan bulat, positif atau negatif dengan panjang tak terbatas
x = 1
y = 25071105226
z = -17081945
print(type(x))
print(type(y))
print(type(z))

#-Float-
#float adalah bilangan positif atau negatif yang mengandung satu atau lebih angka desimal
x = 1.10
y = 1.0
z = -35.59
x = 35e3
y = 12E4
z = -87.7e100

#float juga bisa berupa angka ilmiah dengan huruf'e' untuk menunjukkan pangkat 10
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

#-Complex-
#bilangan complex ditulis dengan huruf 'j' sebagai bagian imaginer
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

#-Angka Acak-
#python memilik modul bawaan random untuk membuat angka acak
import random
print(random.randrange(1, 100))