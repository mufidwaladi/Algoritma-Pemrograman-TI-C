#Fungsi
def get_greeting():
  return "Halo ini hasil percobaan kamu"

message = get_greeting()
print(message) 
#Berguna untuk memecah program agar mempermudah pengembangan
#Bisa mengembalikan nilai dan bisa tidak

#Argumen
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5) 
#contoh argumen dimana memasukkan nilai kepada fungsi
#ada 2 jenis yaitu memasukkan sesuai kata kunci dan sesuai urutan

#Hanya menerima argumen sesuai posisi
def my_function(name, /): #dengan cara menambahkan /
  print("Hello", name)

my_function("Emil") 

#Hanya menerima argumen menggunakan kata kunci
def my_function(*, name): #dengan cara menambahkan * pada bagian awal
  print("Hello", name)

my_function(name = "Emil") 

#menggabungkan 2 jenis argumen dengan syarat
def my_function(a, b, /, *, c, d):
  return a + b + c + d 
#/ melambangkan jenis argumen yang digunakan sebelumnya
#* melambangkan jenis argumen yang digunakan setelahnya

result = my_function(5, 10, c = 15, d = 20)
print(result)

#*args and **kwargs

#*args
#bisa mengmisahkan argumen dari list menjadi individual argumen
#memungkinkan memasukkan jumlah agrumen yang tak terbatas ke dalam fungsi
def tambah_semua(*args):
    total = 0
    for angka in args:
        total += angka
    return total

print(tambah_semua(1, 2))           # Hasil: 3
print(tambah_semua(10, 20, 30, 40)) # Hasil: 100
#dioperasikan sesuai urutan

#**kwargs
#bisa memisahkan argumen dari dictionary
#memasukkan argumen dengan nama dalam jumlah yang fleksibel ke dalam fungsi.
def buat_profil(nama, **kwargs):
    print(f"Nama: {nama}")
    for kunci, nilai in kwargs.items():
        print(f"{kunci}: {nilai}")

# Memanggil fungsi dengan tambahan informasi berbeda
buat_profil("Budi", umur=25, kota="Jakarta")
print("-" * 20)
buat_profil("Siti", hobi="Membaca", status="Mahasiswa", pekerjaan="Penulis")
#dioperasikan sekaligus

#Scope
#Merupakan posisi letak variabel

x = 300 #Global scope
#global scope bisa di gunakan diluar atau didalam sebuah fungsi

def myfunc():
  global x #Mengganti nilai global scope
  x = 200 #Lokal scope
  print(x)

myfunc()

print(x) 

#kata kunci nonlocal
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x #untuk bekerja dengan variabel didalam fungsi berulang
    #berfungsi membuat variabel tersebut menjadi milik fungsi bagian luar
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) 

#Aturan LEGB adalah aturan yang digunakan untuk mencari nilai sebuah variabel.
import builtins # Tempat asal level Built-in

x = "Global"

def luar():
    x = "Enclosing"
    
    def dalam():
        # x = "Local" 
        print(x) # Python akan mencari x di sini
        
    dalam()

luar()

#Decorator
#mengubah atau menambah perilaku sebuah fungsi tanpa harus mengubah kode asli

def my_decorator(func):
    def pembungkus():
        print("Log: Persiapan sebelum eksekusi.")
        
        func()
        
        print("Log: Eksekusi selesai.")
    
    return pembungkus

@my_decorator
def say_hello():
    print("Hello World!")

say_hello()
#note:decorator bisa dengan argumen,decorator bisa digunakan 2 fungsi

#Lambda
#adalah fungsi kecil tanpa nama (anonymous function).
x = lambda a, b : a * b
print(x(5, 6))
#lambda biasanya menjadi "pembantu" bagi fungsi lain.
def myfunc(n):
  return lambda a : a * n 
#seperti pada Fungsi Built-in (Map, Filter, Sorted)

#recursion
#teknik dimana fungsi memanggil dirinya sendiri untuk menyelesaikan masalah.
#syarat agar rekursi berhenti adalah adanya kasus dasar dan langkah rekursif
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5) 
#python memiliki batas rekursif yaitu biasanya 1000 kali

#Generator
#fungsi yang bisa memberhentikan dan melanjutkan eksekusinya
def penghitung_sederhana():
    print("Mulai...")
    yield 1
    yield 2
    yield 3

gen = penghitung_sederhana()

print(next(gen)) # Output: Mulai... 1
print(next(gen)) # Output: 2
print(next(gen)) # Output: 3

#cara kerja:
#mengembalikan sebuah generator object
#lalu dieksekusi setiap kali fungsi next() atau for dipanggil
