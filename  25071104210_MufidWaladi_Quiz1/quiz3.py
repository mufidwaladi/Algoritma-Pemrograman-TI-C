buku = [["Algoritma", 2000],
        ["Basis Data", 2500],
        ["Alpro", 1000],
        ["Strukdat", 1500],
        ["Arsikom", 2500]]

pinjam = [["Algoritma", 2],
        ["Basis Data", 3],
        ["Alpro", 1],
        ["Strukdat", 2],
        ["Arsikom", 1]]

telat = int(input("Masukkan total hari terlambat"))

def cek_hari(telat):
    while telat < 0:
        print("Error masukkan kembali")
        return cek_hari()
    else:
        return True
    
def total_denda(telat):
    if telat == 0:
        print("Tidak ada denda")
    else:
        for i in range(len(pinjam)):    
            total = buku[i][1] * pinjam[i][1]
            print(total)


cek_hari(telat)
if cek_hari(telat) == True:
    total_denda(telat)