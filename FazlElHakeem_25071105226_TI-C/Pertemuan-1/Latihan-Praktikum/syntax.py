#===SYNTAX===

#syntax di python bisa langsung di tulis secara langsung di command line
print("My name is Fazl El Hakeem")

#-Identasi-
#python memakai identasi (tab) untuk menunjukkan blok kode
i = 2
#contoh identasi yang benar
if i % 2 == 0:
   print("genap")
else:
   print("ganjil")

#contoh identasi yang salah (error)
if i % 2 == 0:
print("genap")
else:
print("ganjil")

#jumlah spasi dalam identasi terserah user, setidakny satu atau lebih
if i > 5:
 print(i)
else:
      print(5)

#-Variabel-
#di python variabel dibuat dengan memasukkan nilai ke dalam nya tanpa perlu menulis tipe datanya dulu(python akan otomatis mendeteksi)
i = 23 #integer
j = 23.5 #float
k = "hello" #string
l = True #boolean

#===STATEMENTS===

#dalam bahasa pemrograman, instruksi pemrograman disebut statement, dalam python statement berakhir ketika baris berakhir
#statement tersebut dieksekusi satu  persatu sesuai urutan baris penulisannya
print("hello")
print("how are you?")
print("have a good day")

#kita bisa juga menggunakan semicolon(;) untuk menandai akhir satatement, namun ini jarang digunakan
print("hello"); print("how are you?"); print("have a good day")

