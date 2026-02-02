#match digunakan untuk melakukan aksi berbeda berdasarkan kondisi yang berbeda

#gunakan karakter underscore (_) jika ingin blok kode dieksekusin jika tidak ada kecocokan lain
day = 4
match day:
   case 6:
      print("Today is Saturday")
   case 7:
      print("Today is Sunday")
   case _:
      print("Looking forward to the Weekend")