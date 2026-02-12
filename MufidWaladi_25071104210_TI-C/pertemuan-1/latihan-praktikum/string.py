##String
print("Hello")
#bisa menggunakan ' atau "

#kata di dalam kata
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
#bisa menggunakan "" ataupun '' sebagai pembeda kata

#assigning
a = 'Hello'
print(a) 

#Menggunakan 3 tanda petik
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a) 

#Strings are Arrays
a = "Hello, World!"
print(a[1])
#string sebagai array

#Looping trough a string
for x in "banana":
  print(x)
#melakukan perulangan untuk string sampai karakter terakhir

#String Length
a = "Hello, World!"
print(len(a))
#untuk mengetahui panjang string

#Check String
txt = "The best things in life are free!"
print("free" in txt)
#kita bisa menggunakan in untuk memeriksa apakah dia string bisa juga menggunakan if

#Check if NOT string
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

##Memotong string

b = "Hello, World!"
print(b[2:5])
#menampiljan huruf setelah huruf ke-2 sebagai batas awal
#dan 5 sebagai batas akhir tanpa memasukkan huruf ke 5

#Slice from start
print(b[:5])

#Slice to the end
b = "Hello, World!"
print(b[2:]) 

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])
#dimulai dari akhir string

##Modify String

#Rata Huruf besar
a = "Hello, World!"
print(a.upper())

#Rata Huruf kecil
a = "Hello, World!".lower()
print(a)

#perbedaan penggunaanya yang satu nilainya di convert ketika saat di print
#sedangkan yang satu lagi convertnya saat pengisian variabel

#Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 
#menghilangkan spasi pada awal dan akhir

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#split string
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 
#membelah/memisah string menjadi 2

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
#menggabung 2 variabel

a = "Hello"
b = "World"
c = a + " " + b
print(c)
#menambahkan spasi pada antar string

##String Format
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
# gunakan f string untuk menggabungkan strng dengan variable dan {} untuk meletakkan variabel atau bisa juga untuk melakukan operasi
# :  berfungsi sebagai tanda awal format

#Escape Character
txt = "We are the so-called \"Vikings\" from the north."
#berguna untuk memasukkan karakter yang dilarang di dalam string seperti dia atas

#Simbol,Nama,Kegunaan Utama
#\',Single Quote,Menampilkan tanda kutip satu agar tidak dianggap sebagai penutup kalimat/string.
#\\,Backslash,Menampilkan garis miring terbalik
#\n,New Line,Membuat baris baru
#\r,Carriage Return,Mengembalikan kursor ke bagian awal baris
#\t,Tab,Memberikan jarak horizontal yang lebar (seperti tombol Tab).
#\b Menghapus satu karakter sebelumnya
#\f Menandakan ganti halaman
#\ooo Mewakili karakter berdasarkan angka Oktal
#\xhh Mewakili karakter berdasarkan angka Hexadecimal

#string methods
"""capitalize()	= Merubah Huruf awal menjadi huruf besar
casefold()	= Merubah semua huruf menjadi huruf kecil dan merubah karakter selain kode ASCII
center()	= meletakkan suatu string pada bagian tengah
count()	= menghitung berapa kali muncul sebuah kata yang sama dalam string
encode()	=mengubah string menjadi bentuk bytes.
endswith()	= mengecek apakah sebuah string terdapat akhiran dengan nilai atau karakter tertentu
expandtabs() = mengatur ukuran karakter Tab dalam string dan mengubahnya menjadi spasi
find() = mencari indeks pertama dari kata tertentu pada string.
format() = memasukkan sebuah nilai ke dalam string.
format_map() = memasukkan sebuah nilai yang terdaftar di dictionary ke dalam string 
index()	= mencari indeks pertama dari suatu karakter dalam string yang mengalami error jika gagal
isalnum() = mengecek apakah string hanya terdiri dari karakter alfabet
isalpha()	= mengecek apakah string hanya berisi karakter alfabet (huruf).
isascii()	= mengecek apakah string hanya berisi karakter-karakter yang termasuk dalam tabel ASCII
isdecimal()	= mengecek apakah string hanya berisi karakter angka desimal (0-9).
isdigit()	= apakah seluruh karakter dalam string merupakan karakter angka (digit)
isidentifier() = mengecek apakah sebuah string dapat digunakan sebagai nama dengan sah di dalam Python.
islower()	= apakah semua karakter huruf di dalam sebuah string adalah huruf kecil.
isnumeric()	mengecek apakah semua karakter yang memiliki nilai angka dalam standar Unicode.
isprintable() =	mengecek apakah semua karakter dalam sebuah string dapat dicetak (terlihat) di layar.
isspace()	= mengecek apakah sebuah string hanya berisi karakter spasi atau whitespace.
istitle() = mengecek apakah sebuah string mengikuti format "Title Case" (format penulisan judul).
isupper()	= mengecek apakah semua karakter huruf di dalam string adalah huruf besar (kapital).
join() = menggabungkan elemen-elemen dari urutan (seperti list) menjadi satu string tunggal.
ljust()	= mengatur rata kiri sebuah string dengan menambahkan karakter pengisi hingga mencapai panjang tertentu.
lower()	= mengubah semua huruf kapital di dalam sebuah string menjadi huruf kecil.
lstrip() = menghapus karakter tertentu (biasanya spasi) dari bagian depan sebuah string.
maketrans()	= untuk membuat "tabel pemetaan"
partition()	= membelah string menjadi tiga (dalam sebuah Tuple) berdasarkan pemisah yang ditentukan
replace() = mengganti bagian tertentu dari sebuah string dengan string yang bar
rfind()	= mencari indeks suatu kata di dalam string dari bagian akhir
rindex() = mencari indeks suatu kata di dalam string dari bagian akhir yang mengalami error jika gagal
rjust()	= mengatur rata kanan sebuah string dengan menambahkan karakter pengisi
rpartition()	= membagi string menjadi 3 (tuple), namun pencariannya dimulai dari belakang.
rsplit()	= memecah string menjadi List, dimulai dari akhir string.
rstrip() = menghapus karakter tertentu (terutama spasi) yang berada di akhir string.
split()	= memecah string menjadi List berdasarkan pemisah tertentu.
splitlines() = memecah string berdasarkan baris baru (line breaks).
startswith()	= mengecek apakah string diawali dengan karakter tertentu(Hasilnya selalu bernilai Boolean)
strip()	= pembersih teks yang merupakan gabungan lstrip dan rstrip
swapcase() = membalikkan kondisi huruf dalam string.
title()	= mengubah string menjadi format penulisan judul
translate()	= melakukan penggantian atau penghapusan karakter secara massal berdasarkan instruksi dari tabel pemetaan
upper()	= mengubah semua huruf dalam string menjadi huruf kapital.
zfill()	= untuk menambahkan angka nol (0) di awal string sampai mencapai panjang yang kita inginkan."""
