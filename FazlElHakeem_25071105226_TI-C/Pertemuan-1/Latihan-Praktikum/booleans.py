#tipe data boolean merepresentasikan satu dari dua nilai : True atau False
print(10 > 9)
print(10 == 9)
print(10 < 9)

#-Sebagian Besar Nilai Adalah True-
#semua string adalah True kecuali string kosong
#semua angka adalah True kecuali 0
#semua list, tupple, set, dict adalah True kecuali yang kosong
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#berikut yang akan mengembalikan nilai false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))