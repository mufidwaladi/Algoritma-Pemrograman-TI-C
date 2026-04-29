buku = [["Algoritma", 2000],
        ["Basis Data", 2500],
        ["Alpro", 1000],
        ["Strukdat", 1500],
        ["Arsikom", 2500]]

peminjaman = [[]]

def tambah_pinjaman():
    if pinjam == True:
        judul = input("Masukkan judul")
        for i in range(len(buku)):
            no_buku = buku[i][0]
            if judul == no_buku:
                peminjaman[i].append(buku[i][0])
                lama = int(input("Masukkan lama peminjaman"))
                peminjaman[i].append(lama)
                break
            break

def pinjam():
    pinjam = bool(int(input("Tambahkan buku (1/0)")))
    while pinjam == True:
        tambah_pinjaman()
        return pinjam
    
pinjam()