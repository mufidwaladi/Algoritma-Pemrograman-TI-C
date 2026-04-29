NIM = [2, 5, 0, 7, 1, 1, 0, 4, 2, 1, 0]

def bubble_sort_desc(data):
    n = len(data)
    for i in range(0,n - 1):
    #pengulangan ini berfungsi untuk mengulangi dari 0 hingga akhir
        for j in range(0,n - i - 1):
        #n - i - 1 berfungsi agar tidak mengulangi nilai yang sudah terurut
            if(data[j] < data[j + 1]):
                data[j] , data[j + 1] = data[j + 1], data[j]
                #mengganti data jika angka setelahnya lebih besar
    
    return data

def selection_sort_desc(data):
    n = len(data)
    for i in range(0,n - 1):
    #pengulangan ini berfungsi untuk mengulangi dari 0 hingga akhir
        max_index = 0
        for j in range(0,n - i):
        #n - i berfungsi agar tidak mengulangi nilai yang sudah terurut
            if data[j] < data[max_index]:
                max_index = j
            #mengganti nilai index dari max_index jika lebih kecil dari index ke j 

        data[max_index], data[n - i - 1] = data[n - i - 1], data[max_index]
        #mengurutkan data setelah diselection sort
    
    return data

print("Mengunakan bubble sort")
print(bubble_sort_desc(NIM))
print("Menggunakan selection sort")
print(selection_sort_desc(NIM))