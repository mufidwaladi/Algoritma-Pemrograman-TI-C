#===IF STATEMENT===

#if statement mengevaluasi suatu kondisi, ika  True, blok kode di dalam  if akan dieksekusi.,Jika False, blok kode akan dilewati
a = True 

if a == True:
   print("Benar")


#===ELIF STATEMENT===

#keyword 'elif' adalah cara Python untuk mengatakan "jika kondisi sebelumnya tidak benar, maka coba kondisi ini"
a = 33
b = 33
if b > a:
   print("b is greater than a")
elif a == b:
   print("a and b are equal")


#===ELSE STATEEMENT===

#statement else dieksekusi ketika kondisi if dan kondisi elif  bernilai False
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")