#===VARIABEL PYTHON===

#python tidak memiliki syntax untuk mendeklarasikan variabel
#variabel tercipta saat nilai dimasukkan kedalamnya
x = 10
y = "what are you doing"
print(x)
print(y)

#variabel tidak perlu dideklarasikan dengan tipeda data tertentu, bahkan tipe datanya dapat diubah setelah ditetapkan
x = 178
print(x)
print(type(x))
x = False
print(x)
print(type(x))

#-Casting-
#jika ingin menetukan tipe data suatu variabel dapat dilakukan dengan casting
a = str(9)    #menjadi '9'
b = int(9)    #menjadi 9
c = float(9)  #menjadi 9.0
d = bool(9)   #menjadi True

#-Melihat Tipe Data-
#untuk melihat tipe data suatu variabel dapat menggunakan fungsi type()
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#-Case sensitive-
#nama variabel sesitif terhadap huruf besar dan kecil
p = 345
P = 'Whatsapp'
print(p)
print(P)


#===VARIABEL NAMES===

#aturan penulisan variabel dalam python :
#  *harus diawali dengan huruf atau underscore
#  *tidak boleh diawali dengan angka
#  *hanya boleh berisi karakter alfanumerik dan underscore
#  *variabel peka terhadap huruf besar dan kecil
#  *tidak boleh berupa keyword python apapun

contoh1 = True
contoh_1 = True
_contoh_1 = True
Contoh1 = True
CONTOH1 = True

#-Nama Variabel Multi Words-
#  *Camel case
myVariableName = True
#  *Pascal case
MyVariableName = True
#  *Snake case
my_variable_name = True


#===ASSIGN MULTIPLE VALUES===

#-Banyak Value untuk Multiple Variabel-
x, y, z = 123, 'halo', True
print(x)
print(y)
print(z)

#-Satu Value untuk Multiple Variabel-
x = y = z = 67
print(x)
print(y)
print(z)

#-Unpack Collection-
#kita dapat mengekstrak kumpulan nilai dalam array list atau tuple, proses ini disebut Unpack
vehicle = ['car', 'plane', 'ship']
p, q, r = vehicle
print(p)
print(q)
print(r)


#===OUTPUT VARIABEL===

#fungsi print() sering digunakan untuk menampilkan variabel
o = 'iziiin'
print(o)

#didalam fungsi print() dapat menampilkan beberapa variabel dengan dipisahkan tanda koma
f = 'python'
g = 'javascript'
print(f, g)

#tanda + juga dapat digunakan untuk menampilkan beberapa variabel
print(f + g)

#untuk variabel angka(integer, float) tanda + berfungsi sebagai operator matematika
a = 2
b = 5
print(a + b)

#untuk menampilakn variabel dengan tipe data berbeda lebih baik menggunakan tanda koma(,)
y = 89
z = 'angka'
print(y, z)


#===VARIABEL GLOBAL===

#variabel yang dibuat di luar fungsi dikenal sebagai variabel global, variabel ini dapat digunakan diluar maupun didalam fungsi
c = 'Fazl'

def cetak() :
   print("My name is : " + c)

cetak()

#jika kita membuat variabel yang sama didalam sebuah fungsi, variabel tersebut akan bersifat lokal
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#untuk membuat variabel global didalam fungsi dapat menggunakan keyword global
def contoh():
  global x
  x = "SERU"

contoh()

print("Kuliah taknik itu " + x)

