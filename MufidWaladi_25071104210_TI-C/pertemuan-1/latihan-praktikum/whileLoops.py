#While Loops
i = 1
while i < 6:
  print(i)
  if i == 3:
    break #befungsi menghentikan perulangan
  i += 1
#melakukan perulangan sesuai kondisi yang di berikan

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #menghentikan iterasi sementara lalu di lanjutkan kembali dengan hitungan selanjutnya
  print(i)

#Menggunakan else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#else tidak akan dijalankan jika ada break sebelumnya