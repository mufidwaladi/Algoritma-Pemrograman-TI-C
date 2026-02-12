##Boolean

#memiliki 2 nilai yaitu true and false
print(10 > 9)
print(10 == 9)
print(10 < 9)
#pada python jika kita membandingkan 2 nilai maka dia otomatis menjadi boolean
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 

print(bool("Hello"))
print(bool(15))
#untuk menilai and memberikan True or False

#semua bernilai True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#kecuali string kosong, angka 0,dan semua jenis list yang kosong
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#dan jika Anda memiliki objek yang dibuat dari kelas dengan fungsi __len__ yang mengembalikan 0 atau False
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#fungsi bisa mengembalikan nilai boolean
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") 