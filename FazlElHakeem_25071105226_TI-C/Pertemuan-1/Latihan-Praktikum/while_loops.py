#while loop mengeksekusi serangkaian aksi selama suatu kondisi bernilai True
i = 1
while i < 6:
  print(i)
  i += 1

#-Break-
#break digunakan untuk menghentikan looping walaupun kondisi bernilai True
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#-Continue-
#continue digunakan untuk menghentikan iterasi saat ini dan mlanjutkan ke iterasi berikutnya
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#-Else-
#else digunakan untuk menjalankan blok kode ketika kondisi bernilai False
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")