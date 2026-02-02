#===STRING===

#string di python ditandai dengan tanda kutip tunggal atau ganda

#-Tanda Kutip dalam Tanda Kutip-
#untuk menggunakan tanda kutip di dalam string harus menggunakan tanda kutip yang berbeda dengan yang mengelilingi string tersebut
print("you're ok?")
print('his name is "Budi"')

#-Multiline String-
#kita dapat menetapkan multiline string ke dalam variabel menggunakan triple quotes(""" """)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#-String adalah Array-
#string adalah array karakter unicode, namun python tidak memiliki tipe data karakter, jadi satu karakter adalah string dengan panjang satu
#tanda kurung siku dapat digunakan untuk mengakses elemen dalam string
x = 'Universitas Riau'
print(x[3])

#karena string adalah array, kita bisa looping melalui karakter yang ada di dalam string
x = 'Universitas Riau'
for i in x:
   print(i)

#-Panjang String-
#untuk mengetahui panjang string dapat menggunakan fungsi len()
x = 'Universitas Riau'
print(len(x))

#-Cek String-
#untuk memeriksa apakah suatu karakter ada di dalam string, dapat menggunakan keyword 'in'
teks = "i'm sorry if i say i need you"
print("if" in teks)

#keyword 'not in' digunakan sebagai kebalikan dari 'in'
one = "but i don't care i'm not scare of love"
print("say" not in one)


#===MEMOTONG STRING===
#untuk mengembalikan rentang karakter di string bisa menggunakan sintaks slice
#tentukan indeks awal dan indeks akhir, dipisahkan oleh titik dua, untuk mendapatkan sebagian dari string
b = "you know i want you"
print(b[3:7])

#jika kita menghilangkan indeks awalnya, maka slice akan dimulai dari karakter pertama
c = 'what if we rewrite the stars'
print(c[:10])

#begitu pula jika menghilangkan indeks akhir, slice akan dilakukan sampe karakter terakhir
d = 'all i want is to fly with you'
print(d[4:])


#===MENGGABUNGKAN DUA STRING===

#untk menggabungkan dua string dapat menggunakan operator +
a = 'better'
b = 'than he can'
print("i know i can treat you " + a + b)


#===FORMAT STRING===

#kita dapat menggabungkan string dan angka dengan format() method atau f-string
#untuk menentukan string sebagai f-string cukup letakkan 'f' di depan literal string dan tambahkan kurung kurawal {} sebagai tempat menampung variabel dan operasi lainnya
umur = 18
tes = f"My name is Fazl, I am {age}"
print(tes)


#===ESCAPE CHARACTER===

#untuk menyisipkan karakter tidak sah ke dalam string dapat menggunakan karakter escape berupa backslash (\) diikuti karakter yang ingin dimasukkan 
print("if all of it is \"eight letters\"")


#===STRING METHOD===

#python memiliki banyak metohd bawaan yang dapat digunakan pada string , diantaranya:

#  capitalize() -> membuat karakter pertama menjadi upper case
#  casefold() -> mengubah string menjadi lower case
#  etc