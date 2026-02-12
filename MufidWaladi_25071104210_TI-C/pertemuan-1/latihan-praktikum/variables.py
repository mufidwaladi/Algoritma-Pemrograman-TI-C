#Python_Variables

x = 5
#menjadi variabel karna memasukkan suatu nilai ke dalamnya

y = str(3)
#berfungsi untuk memperjelas tipe data nilainya sama dengan y = '3'

print(type(x))
#berfungsi untuk melihat tipe data dari variable

a = 4
A = 'Sally'
#A tidak akan menggantikan a      

#variable string bisa menggunakan ' ataupun "
q = 'hi '
r = "HI"

#Variable_Names
#Penamaan Variabel harus diawali karatker / garis bawah
#Tidak boleh di awali angka
#hanya boleh menggunakan huruf,angka dan garis bawah
#Besar kecil huruf dapat menjadi pembeda antar variabel
#nama variabel tidak boleh menggunakan syntax python"""

#Untuk variabel yang terdiri dari lebih 2 kata maka bisa menggunakan cara
#camelCase,PascalCase,dan Snake_Case

#Multiple assignment
b, c, d = 'ikan' ,'ayam' ,'sapi'
#python bisa menerima banyak nilai ke banyak variabel dalam 1 baris
b = c = d = 'api streak'
#python bisa memasukkan 1 nilai ke banyak variable

jenis = ['ikan','ayam','sapi']
f, y, z = jenis
#python juga membolehkan mengekstrak nilai variable ke sebuah variable

#Output Variabel
print(q + A)
#berguna untuk menambahkan nilai banyak variable
print(x + a)
#juga otomatis jika bernilai angka terjadi operasi aritmatik
print(r, A)
#perbedaan + dan , pada string dapat di lihat dari penambahan spasi pada ,
#sedangkan + harus menambahkan spasi tersendiri pada nilai variablenya seperti contoh di atas
print(a,A)
#untuk menyatukan angka dan huruf harus menggunakan , tidak bisa menggunakan +

#Global_Variabel
def myfunc():
  global m
  m = "Very Kind"

myfunc()

print("My mom is " + m) 

#global variable sendiri berfungsi agar dapat di akses bebas tanpa harus didalam fungsi