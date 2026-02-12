##Operators

#Operator aritmatika
#berguna untuk melakukan operasi
# + 	Penjumlahan	        x + y 	
# - 	Pengurangan 	    x - y 	
# * 	Perkalian           x * y 	
# / 	Pembagian 	        x / y 	
# % 	Modulus 	        x % y 	
# ** 	Exponensial 	    x ** y 	
# // 	Pembagian lantai 	x // y

#operator masukan
#= 		: Memasukkan Nilai
#+= 	: Menjumlahkan Nilai
#-= 	: Mengurangkan Nilai
#*= 	: Mengalikan Nilai
#/=  	: Membagikan Nilai
#%=  	: Modulokan nilai
#//= 	: Pembagian lantai suatu nilai
#**= 	: Mengeksponensialkan nilai
#&= 	: menggabungkan 2 nilai
#|= 	: Membuat atau pada nilai
#^= 	: Membuat XOR pada nilai
#>>= 	: Menggeser seluruh bit angka ke kanan sebanyak langkah yang ditentukan.
#<<=    : Menggeser seluruh bit angka ke kiri sebanyak langkah yang ditentukan.
#:=     : Memberikan nilai ke variabel sekaligus mengembalikan nilai

# Contoh dar operator :=
input_user = input("Ketik sesuatu: ")
while input_user != "quit":
    print(f"Anda mengetik: {input_user}")
    input_user = input("Ketik sesuatu: ")

#Cara baru
while (input_user := input("Ketik sesuatu: ")) != "quit":
    print(f"Anda mengetik: {input_user}")

#Operator Perbandingan
#==  samadengan
#!=  tidaksamadengan
#>   lebih besar
#<   lebih kecil
#>=  besar samadengan
#<=  kecil samadengan

#Operator Logika
#and  	Mengembalikan Nilai True kalau semua argumen benar		
#or 	    Mengembalikan Nilai True kalau benar salah satu	 	
#not 	Membalikkan hasil

#Operator Identitas
#is mengembalikan True jika semua variabel merupakan objek yang sama
#is not  mengembalikan True jika semua variabel merupakan objek yang beda

#beda dengan samadengan adalah is menganggap sebagai objek yang sama pada memori
#dan samadengan menganggap nilainya setara atau sama

#Operator Anggota
#in         Mengembalikan True jika urutan dengan nilai yang ditentukan ada dalam objek
#not in     Mengembalikan True jika urutan dengan nilai yang ditentukan tidak ada dalam objek

#Bitwise operators
#membandingkan Angka biner
# &(dan) \(atau) ^(exclusive or) -(Not) 
#<< (memasukan angka nol dari kanan kekiri, dan membiarkan paling kiri ilang) 
#>> (memasukan angka nol dari kanan kekiri, dan membiarkan paling kiri ilang)

#Urutan operator
#() 	                                            Parentheses 	
#** 	                                            Exponentiation 	
#+x  -x  ~x 	                                    Unary plus, unary minus, and bitwise NOT 	
#*  /  //  % 	                                    Multiplication, division, floor division, and modulus 	
#+  - 	                                            Addition and subtraction 	
#<<  >> 	                                        Bitwise left and right shifts 	
#& 	                                                Bitwise AND 	
#^ 	                                                Bitwise XOR 	
#| 	                                                Bitwise OR 	
#==  !=  >  >=  <  <=  is  is not  in  not in  	    Comparisons, identity, and membership operators 	
#not 	                                            Logical NOT 	
#and 	                                            AND
#or 	                                            OR