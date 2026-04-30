struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
        }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,"erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
            }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

def total_ukuran(folder: dict) -> int:
    total = 0
    for x in folder.values():
        if type(x) == int:
            total += x
        else:
            total += total_ukuran(x)

    return total

def hitung_file(folder: dict) -> int:
    total = 0
    for x in folder.values():
        if type(x) == int:
            total += 1
        else:
            total += hitung_file(x)

    return total

def cari_terbesar(folder: dict) -> tuple:
    # Kembalikan (nama_file, ukuran_kb)
    Besar = (0, 0)
    for k,v in folder.items():
        if type(v) == int:
            if v > Besar[1]:
                Besar = (k,v)
        else:
            Besar = cari_terbesar(v)

    return Besar

def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    for k, v in folder.items():
        if type(v) == int:
            print(f"{" " * level}📄 {k} ({v} KB)")
        else:
            print(f"{" " * level}📁 {k}")
            tampilkan_tree(v,nama ,level + 4)

print(total_ukuran(struktur))
print(hitung_file(struktur))
print(cari_terbesar(struktur))
tampilkan_tree(struktur)