#perulangan for dapat mengeksekusi serangkaian pernyataan, satu kali untuk setiap item dalam daftar, tuple, set, dan lain sebagainya.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
   print(x)

#-Break-
#dengan statement 'break' kita dapat menghentikan for loop sebelum selesai memproses semua item
fruits = ["apple", "banana", "cherry"]
for x in fruits:
   print(x)
   if x == "banana":
      break

#-Continue- 
#dengan statement 'continue' kita dapat menghentikan iterasi loop dan melanjutkan ke iterasi berikutnya
fruits = ["apple", "banana", "cherry"]
for x in fruits:
   if x == "banana":
      continue
   print(x)

#-range()-
#Fungsi range() mengembalikan serangkaian angka, dimulai dari 0 secara default, dan bertambah 1 , dan berakhir pada angka yang ditentukan
for x in range(6):
   print(x)

#-else-
#keyword 'else' dalam for loop menentukan blok kode yang akan dieksekusi ketika looping selesai
for x in range(6):
   print(x)
else:
   print("Siap!!")

#-Nested Loop-
#nested loop adalah perulangan di dalam perulangan
adj = ["fast", "big", "expensive"]
vehicle = ["car", "plane", "jet"]

for x in adj:
   for y in vehicle:
      print(x, y)
