def input_umur():
    try:
        umur = int(input("Masukkan Umur: ")) 
        print(f"Umur Anda adalah {umur} tahun")
    except ValueError:
        print("Kesalahan: Masukkan angka aja wak, jangan teks")

input_umur()