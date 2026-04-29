DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]
def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    if pilihan_komputer == pilihan_pemain:
        return "seri"
    
    elif pilihan_komputer == "batu" and pilihan_pemain == "kertas" or pilihan_komputer == "gunting" and pilihan_pemain == "batu" or pilihan_komputer == "kertas" and pilihan_pemain == "gunting":
        return "pemain"
    else:
        return "komputer"

def main_satu_giliran(nomor_giliran):
    pilihan_komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)]
    sementara_pilihan_pemain = input("Masukkan (Batu / Kunting / Kertas) :").lower()
    while sementara_pilihan_pemain not in DAFTAR_PILIHAN:
        sementara_pilihan_pemain = input("Masukkan (Batu / Kunting / Kertas) kembali :").lower()
    pilihan_pemain = sementara_pilihan_pemain
    print(f"pilihan komputer adalah {pilihan_komputer}")
    return tentukan_pemenang(pilihan_komputer,pilihan_pemain)
    

def main_satu_ronde(nama, nomor_ronde):
    nomor_giliran = 0
    menang_pemain = 0
    menang_komputer = 0
    while menang_pemain < 3 and menang_komputer < 3:
        nomor_giliran += 1
        ronde = main_satu_giliran(nomor_giliran)
        if ronde == "pemain":
            menang_pemain += 1
        elif ronde == "komputer":
            menang_komputer += 1
        print(menang_pemain)
    hitung_skor = menang_pemain * 10
    return [nama,hitung_skor]

def tampilkan_riwayat(riwayat):    
    if riwayat == None:
        print("Belum ada riwayat")
    else:
        print("| nomor |     Nama     | skor |")
        for i in range(len(riwayat)):
             print(riwayat[i])


def bubble_sort_riwayat(riwayat):
    n = len(riwayat)
    for i in range(0,n - 1):
        for j in range(0,n - i - 1):
            if riwayat[i][1] < riwayat[i+1][1]:
                riwayat[i], riwayat[i+1] = riwayat[i+1] ,riwayat[i]
    return riwayat


def tampilkan_leaderboard(riwayat):
    bubble_sort_riwayat(riwayat)


def main():
    riwayat = []
    nama_pemain = input('Masukkan Nama Pemain :')
    no_ronde = 1
    main_satu_ronde(nama_pemain,no_ronde)
    riwayat.append(main_satu_ronde(nama_pemain,no_ronde))
    bermain = input("Apakah anda ingin bermain kembali ? y/n ")
    while bermain == "y":
        no_ronde += 1
        main_satu_ronde(nama_pemain,no_ronde)
        riwayat.append(main_satu_ronde(nama_pemain,no_ronde))

    tampilkan_riwayat(riwayat)
    tampilkan_leaderboard(riwayat)
if __name__ == "__main__":
    main()