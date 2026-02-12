def rata_rata(nilai):
    if nilai == 0:
        print('data kosong')
    else:
        return jumlah / len(nilai)
    print(nilai)

nilai = [80, 75, 90, 60, 85]
jumlah = 0
for x in nilai :
            jumlah += x
            x + 1

    
mean = rata_rata(nilai)
print(f'Rata ratanya adalah {mean}')