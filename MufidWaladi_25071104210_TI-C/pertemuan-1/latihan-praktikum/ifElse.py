#If Else

#Cara kerja if else adalah jika kondisinya True maka dia akan menjalankan program
#dan jika Kondisinya False maka dia tidak akan menjalankan program

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#dan jangan lupa identation sebagai penanda urutan code dijalankan untuk di dalam if atau bukan
#bisa menggunakan nilai boolean
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

#Elif
#elif berguna untuk mengecek apakah setelah kondisi pertama False ada kondisi lainnya
#atau menambahkan kondisi lain sehingga bernilai True
age = 25
if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

#Else
#adalah dimana tidak adanya kondisi if yang terpenuhi dan bernilai false
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Shorthand ifelse
a = 5
b = 2
if a > b: print("a is greater than b")
#jika hanya if membutuhkan :

a = 2
b = 330
print("A") if a > b else print("B")

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
#variable = nilai true if kondisi else nilai false 

#3 kondisi
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Operator Logika
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")
#beri kurung untuk mempermudah hal kompleks
#untuk memahami cara kerjanya bisa liat tabel kebenaran

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#if didalam if berguna untuk pengecekan berganda pada suatu kondisi

a = 33
b = 200

if b > a:
  pass
#pass berfungsi untuk mencegah if error jika tidak ada kondisi lain