#-Tipe Data Bawaan-
#python memiliki tipe data bawaan secara default dalam kategori berikut:

#  *tipe text : str
#  *tipe Numerik: int, float, complex
#  *tipe Urutan: list, tuple, range
#  *tipe Pemetaan: dict
#  *tipe Set: set, frozenset
#  *tipe Boolean: bool
#  *tipe Biner: bytes, bytearray, memoryview
#  *tidak ada Tipe: NoneType


#-Melihat Tipe Data-
#untuk melihat tipe data dari suatu variabel dapat menggunakan fungsi type()
p = 43
print(type(p))

#-Mengatur Tipe Data Spesifik-
#jika ingin menentukan tipe data dapat menggunakan fungsi konstruktor seperti:
x = str('hahaha')
y = int(34)
z = complex(1j)