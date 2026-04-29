def tot_el(matriks):
    tot = 0
    for baris in matriks:
        for elemen in baris:
            tot += elemen
    return tot

def has_kal(matriks, k):
    hasil = []
    for baris in matriks:
        baris_baru = [elemen * k for elemen in baris]
        hasil.append(baris_baru)
    return hasil

def trans(matriks):
    baris = len(matriks)
    kolom = len(matriks[0])
    hasil = [[0 for _ in range(baris)] for _ in range(kolom)]
    for i in range(baris):
        for j in range(kolom):
            hasil[j][i] = matriks[i][j]
    return hasil

matriks = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

print("Total Manual:", tot_el(matriks))

tot_sing = sum(sum(baris) for baris in matriks)
print("Total cara singkat:",tot_sing)

hasil = has_kal(matriks, 2)
for baris in hasil:
    print(hasil)

t = trans(matriks)
print(t)