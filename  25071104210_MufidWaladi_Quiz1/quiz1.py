buku = [["Algoritma", 2000],
        ["Basis Data", 2500],
        ["Alpro", 1000],
        ["Strukdat", 1500],
        ["Arsikom", 2500]]


i = 1
for daftar in buku:
    print(i ,daftar)
    i += 1


no = int(input("Masukkan nomor buku yang ingin di pilih "))
if no > 5:
    print("Tidak ada pilihan buku")
else:
    for i in range(1,5):
        if i == no:
            print(f"Judul buku : {buku[i-1][0]} Harga denda : {buku[i-1][1]}")

